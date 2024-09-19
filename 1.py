import numpy as np




def compute_dis_mat(self, num_city, location):
    dis_mat = np.zeros((num_city, num_city))# 初始化距离矩阵，城市数量n*n，一个0空矩阵
    for i in range(num_city):
        for j in range(num_city):
            if i == j:
                dis_mat[i][j] = np.inf# 两个城市相同，距离为无穷大
                continue
            a = location[i]# a = (x1,y1)定位坐标
            b = location[j]# b = (x2,y2)定位坐标
            tmp = np.sqrt(sum([(x[0] - x[1]) ** 2 for x in zip(a, b)]))# 计算两个城市之间的距离,a = (x1,y1),b = (x2,y2),使用zip将其压缩成[(x1,x2),(y1,y2)],b-a = (x2-x1,y2-y1)
            dis_mat[i][j] = tmp
    return dis_mat


def compute_pathlen(self, path, dis_mat):
    try:
        a = path[0] # 起点
        b = path[-1]# 终点
    except:
        import pdb
        pdb.set_trace()
    result = dis_mat[a][b]
    for i in range(len(path) - 1):
        a = path[i]
        b = path[i + 1]
        result += dis_mat[a][b]
    return result

# 读取数据
def read_tsp(path):
    lines = open(path, 'r').readlines()
    assert 'NODE_COORD_SECTION\n' in lines
    index = lines.index('NODE_COORD_SECTION\n')
    data = lines[index + 1:-1]
    tmp = []
    for line in data:
        line = line.strip().split(' ')
        if line[0] == 'EOF':
            continue
        tmpline = []
        for x in line:
            if x == '':
                continue
            else:
                tmpline.append(float(x))
        if tmpline == []:
            continue
        tmp.append(tmpline)
    data = tmp
    return data


data = read_tsp('data/st70.tsp')

data = np.array(data)
data = data[:, 1:]
print(data)
# 加上一行因为会回到起点
show_data = np.vstack([data, data[0]])
print(show_data)