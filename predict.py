import tensorflow as tf


CLASSES = ['BANK_TRANSFER', 'MERCHENT', 'MUTUAL_FUND', 'SALARY']

def load_model(model_name: str):
    """
    Returns a loaded model
    """

    return tf.keras.models.load_model(model_name)


if __name__ == '__main__':
    model = load_model('./models/btdl_v0.0')
    preds = model.predict(['UPI P@A @@@@@@@@@@@@ Miss Leah Reed MD Yes Bank UPI'])
    index = tf.argmax(preds, axis=1).numpy()[0]
    print(CLASSES[index] == 'BANK_TRANSFER')