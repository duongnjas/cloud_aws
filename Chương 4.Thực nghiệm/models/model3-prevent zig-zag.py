def reward_function(params):
    '''
    Function phạt lái giúp giảm thiểu hành vi lạng lách đánh võng
    '''
    
    # Nhận thông số đầu vào
    distance_from_center = params['distance_from_center']
    track_width = params['track_width']
    abs_steering = abs(params['steering_angle']) # Only need the absolute steering angle

    # Tính 3 điểm xa và xa hơn khỏi đường tâm
    marker_1 = 0.1 * track_width
    marker_2 = 0.25 * track_width
    marker_3 = 0.5 * track_width

    # Thưởng cao hơn nếu xe gần đường trung tâm hơn và ngược lại
    if distance_from_center <= marker_1:
        reward = 1.0
    elif distance_from_center <= marker_2:
        reward = 0.5
    elif distance_from_center <= marker_3:
        reward = 0.1
    else:
        reward = 1e-3  # đâm / đi chệch hướng

    # Ngưỡng phạt lái, thay đổi số dựa trên cài đặt không gian hành động của bạn
    ABS_STEERING_THRESHOLD = 15 

    #  Phạt nếu xe bẻ lái quá nhiều
    if abs_steering > ABS_STEERING_THRESHOLD:
        reward *= 0.8

    return float(reward)