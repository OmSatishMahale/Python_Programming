import tensorflow as tf

# 0D Tensor(Scalar Tensor)
scalar_tensor = tf.constant(11)
print("Scalar tensor : ",scalar_tensor)

# 1D Tensor (Vector)
vector_tensor = tf.constant([11,21,51,101])
print("Vector Tensor : ",vector_tensor)

# 2D Tensor (Data Frame,Matrix)
matrix_tensor = tf.constant([[10,20,30],[40,50,60]])
print("Matrix Tensor : ",matrix_tensor)

# 3D Tensor
tensor_3d = tf.constant([
    [[1,2],[3,4]],
    [[5,5],[6,6]],
    [[7,8],[9,10]]
])
print("3D Tensor : ",tensor_3d)