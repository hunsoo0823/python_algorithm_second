#from collections import deque

#build_frame = [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]
build_frame = [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]

def possible(result_frame):
    for frame in result_frame:
        x, y, stuff = frame
        
        # 기둥일 경우
        if stuff == 0:
            if y > 0:
                # 기둥이나 보위에 새워야되는 경우
                if ([x, y-1, 0] not in result_frame) and ([x-1, y, 1] not in result_frame) and ([x,y,1] not in result_frame):
                    return False
        # 보일 경우
        elif stuff == 1:
            # 밑에 기둥이 존재하지않거나, 양옆에 보가 없는 경우
            if ([x, y-1, 0] not in result_frame) and ([x+1, y-1, 0] not in result_frame) and (([x-1, y, 1] not in result_frame) or ([x+1, y, 1] not in result_frame)) == True:
                return False

    return True
                
def installation(build_frame):
    result_frame = []
    
    for build in build_frame:
        x, y, a, b = build
        # 구조물을 설치 할때
        if b == 1:
            result_frame.append([x,y,a])
            if possible(result_frame) != True: 
                result_frame.remove([x,y,a])

        # 구조물을 철거할때
        elif b == 0:
            result_frame.remove([x,y,a])
            if possible(result_frame) != True:
                result_frame.append([x,y,a])

    result_frame.sort(key=lambda x : (x[0], x[1]))
    print(result_frame)

installation(build_frame)

