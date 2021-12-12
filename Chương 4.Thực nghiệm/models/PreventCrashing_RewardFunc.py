import math
def reward_function(params):
    '''
    Thưởng cho xe ở trong đường biên và 
    phạt khi đến quá gần các đối tượng khác ở phía trước
    '''
    all_wheels_on_track = params['all_wheels_on_track']
    distance_from_center = params['distance_from_center']
    track_width = params['track_width']
    objects_location = params['objects_location']
    agent_x = params['x']
    agent_y = params['y']
    _, next_object_index = params['closest_objects']
    objects_left_of_center = params['objects_left_of_center']
    is_left_of_center = params['is_left_of_center']

    # Khởi tạo phần thưởng bằng một số nhỏ nhưng không phải số 0 
    # vì số 0 có nghĩa là chệch hướng hoặc gặp sự cố
    reward = 1e-3

    #Thưởng nếu xe ở trong hai biên của đường đua
    if all_wheels_on_track and (0.5 * track_width - distance_from_center) >= 0.05:
        reward_lane = 1.0
    else:
        reward_lane = 1e-3
    # Phạt nếu xe ở quá gần đối tượng tiếp theo
    reward_avoid = 1.0

    # Khoảng cách đến đối tượng khác
    next_object_loc = objects_location[next_object_index]
    distance_closest_object = math.sqrt((agent_x - next_object_loc[0])**2 + (agent_y - next_object_loc[1])**2)
    
    # Quyết định xem xe và đối tượng tiếp theo có trên cùng một làn đường hay không
    is_same_lane = objects_left_of_center[next_object_index] == is_left_of_center
    if is_same_lane:
        if 0.5 <= distance_closest_object < 0.8:
            reward_avoid *= 0.5
        elif 0.3 <= distance_closest_object < 0.5:
            reward_avoid *= 0.2
        elif distance_closest_object < 0.3:
            reward_avoid = 1e-3  # Likely crashed

    # Tính phần thưởng bằng cách đặt các trọng số khác nhau cho 
    # hai khía cạnh ở trên
    reward += 1.0 * reward_lane + 4.0 * reward_avoid
    return reward