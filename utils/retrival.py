"""
does some data changes
"""
import os
import numpy as np
import matplotlib.pyplot as plt

# all 2468 shapes
TOP_K = 1000


def append_feature(raw, data, flaten=False):
    """

    :param raw:
    :param data:
    :param flaten:
    :return:
    """
    data = np.array(data)
    if flaten:
        data = data.reshape(-1, 1)
    if raw is None:
        raw = np.array(data)
    else:
        raw = np.vstack((raw, data))
    return raw


def eu_dis_mat_fast(x):
    """

    :param x:
    :return:
    """
    a_a = np.sum(np.multiply(x, x), 1)
    a_b = x*x.T
    d = a_a+a_a.T - 2*a_b
    d[d < 0] = 0
    d = np.sqrt(d)
    d = np.maximum(d, d.T)
    return d


def calculate_map(fts, lbls, dis_mat=None):
    """

    :param fts:
    :param lbls:
    :param dis_mat:
    :return:
    """
    if dis_mat is None:
        dis_mat = eu_dis_mat_fast(np.mat(fts))
    num = len(lbls)
    map_ = 0
    for i in range(num):
        scores = dis_mat[:, i]
        targets = (lbls == lbls[i]).astype(np.uint8)
        sortind = np.argsort(scores, 0)[:TOP_K]
        truth = targets[sortind]
        summ = 0
        precision = []
        for j in range(TOP_K):
            if truth[j]:
                summ+=1
                precision.append(summ*1.0/(j + 1))
        if len(precision) == 0:
            a_p = 0
        else:
            for i_i in range(len(precision)):
                precision[i_i] = max(precision[i_i:])
            a_p = np.array(precision).mean()
        map_ += a_p
    map_ = map_/num
    return map_


def cal_pr(cfg, des_mat, lbls, save=True, draw=False):
    """
    calculates precision?
    :param cfg:
    :param des_mat:
    :param lbls:
    :param save:
    :param draw:
    :return:
    """
    num = len(lbls)
    precisions = []
    recalls = []
    ans = []
    for i in range(num):
        scores = des_mat[:, i]
        targets = (lbls == lbls[i]).astype(np.uint8)
        sortind = np.argsort(scores, 0)[:TOP_K]
        truth = targets[sortind]
        tmp = 0
        summ = truth[:TOP_K].sum()
        precision = []
        recall = []
        for j in range(TOP_K):
            if truth[j]:
                tmp += 1
            recall.append(tmp*1.0/summ)
            precision.append(tmp*1.0/(j+1))
        precisions.append(precision)
        for j in range(len(precision)):
            precision[j] = max(precision[j:])
        recalls.append(recall)
        tmp = []
        for ii in range(11):
            min_des = 100
            val = 0
            for j in range(TOP_K):
                if abs(recall[j] - ii * 0.1) < min_des:
                    min_des = abs(recall[j] - ii * 0.1)
                    val = precision[j]
            tmp.append(val)
        print('%d/%d' % (i+1, num))
        ans.append(tmp)
    ans = np.array(ans).mean(0)
    if save:
        save_dir = os.path.join(cfg.result_sub_folder, 'pr.csv')
        np.savetxt(save_dir, np.array(ans), fmt='%.3f', delimiter=',')
    if draw:
        plt.plot(ans)
        plt.show()


def test():
    """
    performs some testing
    :return:
    """
    scores = [0.23, 0.76, 0.01, 0.91, 0.13, 0.45, 0.12, 0.03,
              0.38, 0.11, 0.03, 0.09, 0.65, 0.07, 0.12, 0.24, 0.1, 0.23, 0.46, 0.08]
    gt_label = [0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1]
    scores = np.array(scores)
    targets = np.array(gt_label).astype(np.uint8)
    sortind = np.argsort(scores, 0)[::-1]
    truth = targets[sortind]
    sum = 0
    precision = []
    for j in range(20):
        if truth[j]:
            sum += 1
            precision.append(sum / (j + 1))
    if len(precision) == 0:
        a_p = 0
    else:
        for i in range(len(precision)):
            precision[i] = max(precision[i:])
        a_p = np.array(precision).mean()
    print(a_p)


if __name__ == '__main__':
    test()
