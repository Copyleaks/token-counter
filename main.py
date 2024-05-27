import math
import os
from lexer_resolver import LexerResolver
from token_counter import TokenCounter
from tqdm import tqdm
import concurrent.futures
from collections import defaultdict
import requests
import sys
import argparse

ARG_PARSER = argparse.ArgumentParser()
ARG_PARSER.add_argument("--directory", "-d" , help="Directory to scan for source code files", required= True)

def get_files(directory):
    files = []
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Get the total number of directories to process
        total_directories = sum(1 for _ in os.walk(directory))
        
        # Create a tqdm progress bar
        with tqdm(total=total_directories, desc='Getting files') as pbar:
            # Use executor.map to parallelize the os.walk operation
            results = executor.map(lambda args: [os.path.join(args[0], file) for file in args[2]], os.walk(directory))
            
            for result in results:
                files.extend(result)
                pbar.update(1)
    
    return files

def process_file(file):
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
        return TokenCounter.count_tokens(LexerResolver.get_lexer_for_filetype(file), content)

def count_tokens(supported_files):
    total_token_count = 0

    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = list(executor.map(process_file, supported_files)) # Use tqdm to display a progress bar

    total_token_count = sum(results)
    average_token_count = math.ceil(total_token_count / len(supported_files))

    return total_token_count, average_token_count
                

def group_files_by_type(file_paths):
    grouped_files = defaultdict(list)

    for file_path in file_paths:
        file_type = os.path.splitext(file_path)[1].lower()  # Get the file extension
        grouped_files[file_type].append(file_path)

    return dict(grouped_files)

def get_copyleaks_supported_filetypes():
    response = requests.get('https://api.copyleaks.com/v3/miscellaneous/supported-file-types')
    if not response.ok:
        raise LookupError("Unable to read supported filetypes from Copyleaks API.")
    
    return response.json()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(ARG_PARSER.print_help())
        raise ValueError("Please provide a directory to scan.")
    
    if sys.argv[1] == '-h' or sys.argv[1] == '--help':
        print(ARG_PARSER.print_help())
        sys.exit()
    
    if sys.argv[1] != '-d' or sys.argv[1] == '--directory':
        print("please provide a valid argument.")
        print(ARG_PARSER.print_help())
        sys.exit()
    
    args = ARG_PARSER.parse_args()

    if not os.path.isdir(args.directory):
        raise ValueError("The provided directory does not exist.")
    
    all_files = get_files(args.directory)
    print(f'{"{:,}".format(len(all_files))} files found')

    files_by_types = group_files_by_type(all_files)

    copyleaks_supported_filetypes = get_copyleaks_supported_filetypes()

    for extension in files_by_types:
        if LexerResolver.is_file_extension_supported(files_by_types[extension][0]):
            print (f'*{extension}:')
            print(f'\tFiles: {"{:,}".format(len(files_by_types[extension]))}')
            token_count, average_token_count = count_tokens(files_by_types[extension])
            print(f'\tTokens: {"{:,}".format(token_count)}')
            print(f'\tAverage Token count: {"{:,}".format(average_token_count)}')
            print()