import pandas as pd

def filter_data(model_data, user_height, user_weight, user_gender, error_range=1):
    
    model_data['height'] = pd.to_numeric(model_data['height'], errors='coerce')
    model_data['weight'] = pd.to_numeric(model_data['weight'], errors='coerce')

    min_height = user_height - error_range
    max_height = user_height + error_range
    min_weight = user_weight - error_range
    max_weight = user_weight + error_range

    if user_gender == 'male':
        filtered_data = model_data[(model_data['height'] >= min_height) & (model_data['height'] <= max_height) &
                             (model_data['weight'] >= min_weight) & (model_data['weight'] <= max_weight) &
                             (model_data['gender'] == 'M')]
    elif user_gender == 'female':
        filtered_data = model_data[(model_data['height'] >= min_height) & (model_data['height'] <= max_height) &
                             (model_data['weight'] >= min_weight) & (model_data['weight'] <= max_weight) &
                             (model_data['gender'] == 'F')]
    else:
        print("올바른 성별을 입력하세요 (M 또는 F).")
        return None

    return filtered_data
