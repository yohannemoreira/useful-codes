def save_array_as_pickle(array, file_path):
    import pickle
    with open(file_path, 'wb') as f:
        pickle.dump(array, f)

def load_pickle_file(file_path):
    import pickle
    with open(file_path, 'rb') as f:
        return pickle.load(f)
