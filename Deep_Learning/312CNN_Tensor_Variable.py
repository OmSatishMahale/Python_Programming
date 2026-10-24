import tensorflow as tf

weight = tf.Variable(5.0)

print("Initial weight value : ",weight.numpy())

weight.assign(10.0)
print("Updated Weight : ",weight.numpy())

weight.assign_add(2.5)
print("Updated Weight : ",weight.numpy())

weight.assign_sub(1.5)
print("Updated Weight : ",weight.numpy())