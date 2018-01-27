# TensorFlow 라이브러리를 추가한다.
import tensorflow as tf
import numpy as np

np.random.seed(20160704)
tf.set_random_seed(20160704)

def op2Numpy(op):
    sess = tf.InteractiveSession()
    init = tf.global_variables_initializer()
    sess.run(init)
    ret = sess.run(op)
    sess.close()

    return ret



IRIS_TRAINING = "tra1.csv"
IRIS_TEST = "tes1.csv"

score = tf.Variable(initial_value=0.0, name="score",dtype=tf.float32)

# 데이터셋을 불러옵니다.
training_set = tf.contrib.learn.datasets.base.load_csv_with_header(
    filename=IRIS_TRAINING,
    target_dtype=np.int,
    features_dtype=np.float32)
test_set = tf.contrib.learn.datasets.base.load_csv_with_header(
    filename=IRIS_TEST,
    target_dtype=np.int,
    features_dtype=np.float32)
plus_training = tf.contrib.learn.datasets.base.load_csv_with_header(
    filename="tra2.csv",
    target_dtype=np.int,
    features_dtype=np.float32)
plus_test = tf.contrib.learn.datasets.base.load_csv_with_header(
    filename="tes2.csv",
    target_dtype=np.int,
    features_dtype=np.float32)

# 모든 특성이 실수값을 가지고 있다고 지정합니다



x = tf.placeholder(tf.float32, [None, 9216])

x_image = tf.reshape(x, [-1,96,96,1])

num_filters1 = 32
W_conv1 = tf.Variable(tf.truncated_normal([5,5,1,num_filters1],stddev=0.1)) #[5,5]:커널크기, 1:입력값x의 특성수, num_filter1: 필터갯수
h_conv1 = tf.nn.conv2d(x_image, W_conv1,strides=[1,1,1,1], padding='SAME') # SAME옵션 : 크기를 패딩값을 이용해 보존
b_conv1 = tf.Variable(tf.constant(0.1, shape=[num_filters1]))
h_conv1_cutoff = tf.nn.relu(h_conv1 + b_conv1)
h_pool1 = tf.nn.max_pool(h_conv1_cutoff, ksize=[1,2,2,1],strides=[1,2,2,1], padding='SAME')

# define second layer
num_filters2a = 64
W_conv2a = tf.Variable(tf.truncated_normal([5,5,num_filters1,num_filters2a],stddev=0.1))
h_conv2a = tf.nn.conv2d(h_pool1, W_conv2a,strides=[1,1,1,1], padding='SAME')
b_conv2a = tf.Variable(tf.constant(0.1, shape=[num_filters2a]))
h_conv2_cutoffa = tf.nn.relu(h_conv2a + b_conv2a)
h_pool2a = tf.nn.max_pool(h_conv2_cutoffa, ksize=[1,2,2,1],strides=[1,2,2,1], padding='SAME')

# define 3th layer
num_filters2b = 32
W_conv2b = tf.Variable(tf.truncated_normal([5,5,num_filters2a,num_filters2b],stddev=0.1))
h_conv2b = tf.nn.conv2d(h_pool2a, W_conv2b,strides=[1,1,1,1], padding='SAME')
b_conv2b = tf.Variable(tf.constant(0.1, shape=[num_filters2b]))
h_conv2_cutoffb = tf.nn.relu(h_conv2b + b_conv2b)
h_pool2b = tf.nn.max_pool(h_conv2_cutoffb, ksize=[1,2,2,1],strides=[1,2,2,1], padding='SAME')

# define 4th layer
num_filters2c = 32
W_conv2c = tf.Variable(tf.truncated_normal([5,5,num_filters2b,num_filters2c],stddev=0.1))
h_conv2c = tf.nn.conv2d(h_pool2b, W_conv2c,strides=[1,1,1,1], padding='SAME')
b_conv2c = tf.Variable(tf.constant(0.1, shape=[num_filters2c]))
h_conv2_cutoffc = tf.nn.relu(h_conv2c + b_conv2c)
h_pool2c = tf.nn.max_pool(h_conv2_cutoffc, ksize=[1,2,2,1],strides=[1,2,2,1], padding='SAME')

# define 5th layer
num_filters2 = 64
W_conv2 = tf.Variable(tf.truncated_normal([5,5,num_filters2c,num_filters2],stddev=0.1))
h_conv2 = tf.nn.conv2d(h_pool2c, W_conv2,strides=[1,1,1,1], padding='SAME')
b_conv2 = tf.Variable(tf.constant(0.1, shape=[num_filters2]))
h_conv2_cutoff = tf.nn.relu(h_conv2 + b_conv2)
h_pool2 = tf.nn.max_pool(h_conv2_cutoff, ksize=[1,2,2,1],strides=[1,2,2,1], padding='SAME')

# define fully connected layer
pl = tf.placeholder(tf.float32, [None, 5])

h_pool2_flat = tf.reshape(h_pool2, [-1,3*3*num_filters2])

h_pool2_flat = tf.concat( [h_pool2_flat, pl], 1 )
num_units1 = 3*3*num_filters2 + 5
num_units2 = 1024
w2 = tf.Variable(tf.truncated_normal([num_units1, num_units2]))
b2 = tf.Variable(tf.constant(0.1, shape=[num_units2]))

hidden2 = tf.nn.relu(tf.matmul(h_pool2_flat, w2) + b2)
keep_prob = tf.placeholder(tf.float32)
hidden2_drop = tf.nn.dropout(hidden2, keep_prob)
w0 = tf.Variable(tf.zeros([num_units2, 4]))
b0 = tf.Variable(tf.zeros([4]))
k = tf.matmul(hidden2_drop, w0) + b0
p = tf.nn.softmax(k)

#define loss (cost) function
t = tf.placeholder(tf.float32, [None, 4])
loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=k,labels=t))
train_step = tf.train.AdamOptimizer(0.0001).minimize(loss)
#correct_prediction = tf.equal(tf.argmax(p, 1), tf.argmax(t, 1))
#accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

# 경사하강법으로 모델을 학습한다.
init = tf.global_variables_initializer()

print("Training")

saver = tf.train.Saver()

with tf.Session() as sess:
    sess.run(init)

    for i in range(0,600) :
        print(i)
        sess.run(train_step, feed_dict={x: np.reshape(training_set.data[i], (-1,9216)),
                                        t: np.reshape(op2Numpy(tf.one_hot(int((int(training_set.target[i]))/10),4,on_value=1,off_value=0,axis=-1)),(-1,4)),
                                        pl: np.reshape(plus_training.data[i], (-1,5)),
                                        keep_prob:0.5})
    saver.save(sess,'/tmp/5layer_600data')


    # 학습된 모델이 얼마나 정확한지를 출력한다.

    #saver.restore(sess, '/tmp/5layer_600data')

    y = tf.nn.softmax(k)
    res = tf.argmax(y,1)
    correct_prediction = tf.equal(tf.argmax(y,1), tf.argmax(t,1))
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
    score = tf.assign(score,score+accuracy)

    for i in range(0,1000):
        print(sess.run([res, y,t, score/(i+1)], feed_dict={x: np.reshape(test_set.data[i], (-1,9216)),
                                                                t: np.reshape(op2Numpy(tf.one_hot(int(int((test_set.target[i]))/10),4,on_value=1,off_value=0,axis=-1)),(-1,4)),
                                                                pl: np.reshape(plus_test.data[i], (-1,5)),
                                                                keep_prob:0.5}))
        if(sess.run(res[0], feed_dict={x: np.reshape(test_set.data[i], (-1, 9216)),
                                                                t: np.reshape(op2Numpy(
                                                                    tf.one_hot(int(int((test_set.target[i])) / 10), 4,
                                                                               on_value=1, off_value=0, axis=-1)),
                                                                              (-1, 4)),
                                                                pl: np.reshape(plus_test.data[i], (-1, 5)),
                                                                keep_prob: 0.5})==0) : print("yes")
sess.close()