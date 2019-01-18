{"nbformat":4,"nbformat_minor":0,"metadata":{"colab":{"name":"Copy of mnistipynb","version":"0.3.2","provenance":[{"file_id":"10o9mYbgCwXyamKLScSqrXJNcSs6W1puK","timestamp":1543301373224}]},"kernelspec":{"name":"python3","display_name":"Python 3"},"accelerator":"TPU"},"cells":[{"metadata":{"id":"bhcllnYY0wBL","colab_type":"code","colab":{"base_uri":"https://localhost:8080/","height":269},"outputId":"960ed2d0-c8fa-4516-b28d-d7cb4ff42035","executionInfo":{"status":"ok","timestamp":1543299969204,"user_tz":-330,"elapsed":92086,"user":{"displayName":"RISHABH CHAKARABARTY","photoUrl":"","userId":"12942336028013708336"}}},"cell_type":"code","source":["import tensorflow as tf\n","mnist = tf.keras.datasets.mnist\n","\n","(x_train, y_train),(x_test, y_test) = mnist.load_data()\n","x_train, x_test = x_train / 255.0, x_test / 255.0\n","\n","model = tf.keras.models.Sequential([\n","  tf.keras.layers.Flatten(),\n","  tf.keras.layers.Dense(512, activation=tf.nn.relu),\n","  tf.keras.layers.Dropout(0.2),\n","  tf.keras.layers.Dense(10, activation=tf.nn.softmax)\n","])\n","model.compile(optimizer='adam',\n","              loss='sparse_categorical_crossentropy',\n","              metrics=['accuracy'])\n","\n","model.fit(x_train, y_train, epochs=5)\n","model.evaluate(x_test, y_test)"],"execution_count":1,"outputs":[{"output_type":"stream","text":["Downloading data from https://storage.googleapis.com/tensorflow/tf-keras-datasets/mnist.npz\n","11493376/11490434 [==============================] - 0s 0us/step\n","Epoch 1/5\n","60000/60000 [==============================] - 17s 289us/step - loss: 0.1999 - acc: 0.9419\n","Epoch 2/5\n","60000/60000 [==============================] - 16s 272us/step - loss: 0.0809 - acc: 0.9750\n","Epoch 3/5\n","60000/60000 [==============================] - 16s 270us/step - loss: 0.0507 - acc: 0.9843\n","Epoch 4/5\n","60000/60000 [==============================] - 16s 264us/step - loss: 0.0356 - acc: 0.9887\n","Epoch 5/5\n","60000/60000 [==============================] - 16s 268us/step - loss: 0.0276 - acc: 0.9910\n","10000/10000 [==============================] - 1s 61us/step\n"],"name":"stdout"},{"output_type":"execute_result","data":{"text/plain":["[0.07685876322116238, 0.9775]"]},"metadata":{"tags":[]},"execution_count":1}]},{"metadata":{"id":"50MdaMj92OH8","colab_type":"code","colab":{"base_uri":"https://localhost:8080/","height":35},"outputId":"f8a2bf82-e828-4c28-cec1-6c725042f55d","executionInfo":{"status":"ok","timestamp":1543299990584,"user_tz":-330,"elapsed":1820,"user":{"displayName":"RISHABH CHAKARABARTY","photoUrl":"","userId":"12942336028013708336"}}},"cell_type":"code","source":["pwd"],"execution_count":2,"outputs":[{"output_type":"execute_result","data":{"text/plain":["'/content'"]},"metadata":{"tags":[]},"execution_count":2}]},{"metadata":{"id":"ud-wd9AY2RPD","colab_type":"code","colab":{"base_uri":"https://localhost:8080/","height":35},"outputId":"8f3c7d53-bf75-412f-ac43-6cb93c724a55","executionInfo":{"status":"ok","timestamp":1543300008818,"user_tz":-330,"elapsed":1742,"user":{"displayName":"RISHABH CHAKARABARTY","photoUrl":"","userId":"12942336028013708336"}}},"cell_type":"code","source":["cd\n"],"execution_count":3,"outputs":[{"output_type":"stream","text":["/root\n"],"name":"stdout"}]},{"metadata":{"id":"Vf9jFJr62VMz","colab_type":"code","colab":{}},"cell_type":"code","source":["mkdir mnist"],"execution_count":0,"outputs":[]},{"metadata":{"id":"uGuwEM7H2gT6","colab_type":"code","colab":{"base_uri":"https://localhost:8080/","height":35},"outputId":"f668ae3a-a4c1-4980-b0da-aa7f90f5e25b","executionInfo":{"status":"ok","timestamp":1543300074421,"user_tz":-330,"elapsed":2025,"user":{"displayName":"RISHABH CHAKARABARTY","photoUrl":"","userId":"12942336028013708336"}}},"cell_type":"code","source":["cd mnist"],"execution_count":5,"outputs":[{"output_type":"stream","text":["/root/mnist\n"],"name":"stdout"}]},{"metadata":{"id":"UlxmTmNY2lMK","colab_type":"code","colab":{"base_uri":"https://localhost:8080/","height":71},"outputId":"02535f81-ade7-4247-fe8e-eff60ca91caa","executionInfo":{"status":"ok","timestamp":1543300105757,"user_tz":-330,"elapsed":8299,"user":{"displayName":"RISHABH CHAKARABARTY","photoUrl":"","userId":"12942336028013708336"}}},"cell_type":"code","source":["!curl https://raw.githubusercontent.com/rohan-varma/rohan-blog/master/images/mnistimg.png > img1.jpg"],"execution_count":7,"outputs":[{"output_type":"stream","text":["  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current\n","                                 Dload  Upload   Total   Spent    Left  Speed\n","\r  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0\r100 26256  100 26256    0     0  79563      0 --:--:-- --:--:-- --:--:-- 79805\n"],"name":"stdout"}]},{"metadata":{"id":"sTq2nNpt2uUj","colab_type":"code","colab":{"base_uri":"https://localhost:8080/","height":1007},"outputId":"8919e558-883a-4aca-d33e-a9fe0cba3288"},"cell_type":"code","source":["import tensorflow as tf\n","mnist = tf.keras.datasets.mnist\n","\n","(x_train, y_train),(x_test, y_test) = mnist.load_data()\n","x_train, x_test = x_train / 255.0, x_test / 255.0\n","print(x_test)\n","\n","model = tf.keras.models.Sequential([\n","  tf.keras.layers.Flatten(),\n","  tf.keras.layers.Dense(512, activation=tf.nn.relu),\n","  tf.keras.layers.Dropout(0.2),\n","  tf.keras.layers.Dense(10, activation=tf.nn.softmax)\n","])\n","model.compile(optimizer='adam',\n","              loss='sparse_categorical_crossentropy',\n","              metrics=['accuracy'])\n","\n","model.fit(x_train, y_train, epochs=5)\n","model.evaluate(x_test, y_test)"],"execution_count":0,"outputs":[{"output_type":"stream","text":["[[[0. 0. 0. ... 0. 0. 0.]\n","  [0. 0. 0. ... 0. 0. 0.]\n","  [0. 0. 0. ... 0. 0. 0.]\n","  ...\n","  [0. 0. 0. ... 0. 0. 0.]\n","  [0. 0. 0. ... 0. 0. 0.]\n","  [0. 0. 0. ... 0. 0. 0.]]\n","\n"," [[0. 0. 0. ... 0. 0. 0.]\n","  [0. 0. 0. ... 0. 0. 0.]\n","  [0. 0. 0. ... 0. 0. 0.]\n","  ...\n","  [0. 0. 0. ... 0. 0. 0.]\n","  [0. 0. 0. ... 0. 0. 0.]\n","  [0. 0. 0. ... 0. 0. 0.]]\n","\n"," [[0. 0. 0. ... 0. 0. 0.]\n","  [0. 0. 0. ... 0. 0. 0.]\n","  [0. 0. 0. ... 0. 0. 0.]\n","  ...\n","  [0. 0. 0. ... 0. 0. 0.]\n","  [0. 0. 0. ... 0. 0. 0.]\n","  [0. 0. 0. ... 0. 0. 0.]]\n","\n"," ...\n","\n"," [[0. 0. 0. ... 0. 0. 0.]\n","  [0. 0. 0. ... 0. 0. 0.]\n","  [0. 0. 0. ... 0. 0. 0.]\n","  ...\n","  [0. 0. 0. ... 0. 0. 0.]\n","  [0. 0. 0. ... 0. 0. 0.]\n","  [0. 0. 0. ... 0. 0. 0.]]\n","\n"," [[0. 0. 0. ... 0. 0. 0.]\n","  [0. 0. 0. ... 0. 0. 0.]\n","  [0. 0. 0. ... 0. 0. 0.]\n","  ...\n","  [0. 0. 0. ... 0. 0. 0.]\n","  [0. 0. 0. ... 0. 0. 0.]\n","  [0. 0. 0. ... 0. 0. 0.]]\n","\n"," [[0. 0. 0. ... 0. 0. 0.]\n","  [0. 0. 0. ... 0. 0. 0.]\n","  [0. 0. 0. ... 0. 0. 0.]\n","  ...\n","  [0. 0. 0. ... 0. 0. 0.]\n","  [0. 0. 0. ... 0. 0. 0.]\n","  [0. 0. 0. ... 0. 0. 0.]]]\n","Epoch 1/5\n","60000/60000 [==============================] - 18s 297us/step - loss: 0.2007 - acc: 0.9405\n","Epoch 2/5\n","60000/60000 [==============================] - 16s 274us/step - loss: 0.0803 - acc: 0.9756\n","Epoch 3/5\n","36352/60000 [=================>............] - ETA: 6s - loss: 0.0514 - acc: 0.9837"],"name":"stdout"}]}]}