def reward_function(params):
    '''
    Thưởng theo đường trung tâm
    Xác định khoảng cách từ xe đến trung tâm và 
    thưởng cao hơn nếu xe ở gần trung tâm hơn
    (khuyến khích xe theo sát đường trung tâm)
    '''
    
    # Nhận thông số đầu vào
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']

    # Tính 3 điểm đánh dấu ngày càng xa đường chính giữa 
    marker_1 = 0.1 * track_width
    marker_2 = 0.25 * track_width
    marker_3 = 0.5 * track_width

    # Cho điểm cao hơn nếu xe gần đường trung tâm hơn và ngược lại
    if distance_from_center <= marker_1:
        reward = 1
    elif distance_from_center <= marker_2:
        reward = 0.5
    elif distance_from_center <= marker_3:
        reward = 0.1
    else:
        reward = 1e-3  #đâm / đi chệch hướng

    return reward