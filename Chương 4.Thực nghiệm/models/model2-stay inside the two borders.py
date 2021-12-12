def reward_function(params):
    '''
    Thưởng khi xe lại trong hai đường biên của đường đua
    '''
    
    # Nhận thông số đầu vào
    all_wheels_on_track = params['all_wheels_on_track']
    distance_from_center = params['distance_from_center']
    track_width = params['track_width']
    
    # Mặc định là đưa ra phần thưởng rất thấp 
    reward = 1e-3

    # Trao phần thưởng cao nếu không có bánh xe nào chệch khỏi đường đua và 
    # chiếc ô tô đang ở đâu đó giữa biên giới đường đua
    if all_wheels_on_track and (0.5*track_width - distance_from_center) >= 0.05:
        reward = 1.0

    return reward