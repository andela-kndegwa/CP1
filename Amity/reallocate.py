for allocation in allocations:
        if allocation[person_id] and allocation[person_id]\
                in rooms['offices'] and room_type == 'O':
            msg = 'Person ID %s was formerly allocated ' % person_id
            msg += 'to the office %s. \n' % allocation[person_id]
            prev_room = allocation[person_id]
            for room in range(len(all_rooms)):
                if allocation[person_id] == all_rooms[room]['room_name']:
                    if len(all_rooms[room]['occupants']) < 6:
                        all_rooms[room]['occupants'].append(person_id)
                    else:
                        return 'Maximum capacity reached'
            allocation[person_id] = offices[randint(0, (len(offices) - 1))]
            new_room = allocation[person_id]
            while prev_room == new_room:
                for room in range(len(all_rooms)):
                    if allocation[person_id] == all_rooms[room]['room_name']:
                        if len(all_rooms[room]['occupants']) < 6:
                            all_rooms[room]['occupants'].append(person_id)
                        else:
                            return 'Maximum capacity reached'
                allocation[person_id] = offices[randint(0, (len(offices) - 1))]
            msg += 'New office allocated is %s' % allocation[person_id]
            return msg
        elif allocation[person_id] and allocation[person_id] \
                in rooms['livingSpaces'] and room_type == 'L':
            msg = 'Person ID %s was formerly allocated ' % person_id
            msg += 'to the living space %s \n' % allocation[person_id]
            prev_room = allocation[person_id]
            for room in range(len(all_rooms)):
                if allocation[person_id] == all_rooms[room]['room_name']:
                    if len(all_rooms[room]['occupants']) < 6:
                        all_rooms[room]['occupants'].append(person_id)
                    else:
                        return 'Maximum capacity reached'
            allocation[person_id] = living_spaces[
                randint(0, (len(living_spaces) - 1))]
            new_room = allocation[person_id]
            while prev_room == new_room:
                for room in range(len(all_rooms)):
                    if allocation[person_id] == all_rooms[room]['room_name']:
                        if len(all_rooms[room]['occupants']) < 6:
                            all_rooms[room]['occupants'].append(person_id)
                        else:
                            return 'Maximum capacity reached'
                allocation[person_id] = living_spaces[
                    randint(0, (len(living_spaces) - 1))]
            msg += 'New living space allocated is %s' % allocation[person_id]
            return msg
    return allocations