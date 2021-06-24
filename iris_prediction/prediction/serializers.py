from rest_framework import serializers
from .models import Flower
import pandas as pd


class FlowerSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        # Get the required data and read the pickled data to make
        # prediction and save it with the result
        sepal_length = self.validated_data.get('sepal_length')
        sepal_width = self.validated_data.get('sepal_width')
        petal_length = self.validated_data.get('petal_length')
        petal_width = self.validated_data.get('petal_width')
        model = pd.read_pickle(r'/home/tanmay/iris_prediction/iris_prediction/new_model.pickle')
        result = model.predict([[sepal_length, sepal_width, petal_length, petal_width]])
        classification = result[0]
        return Flower.objects.create(sepal_length=sepal_length, sepal_width=sepal_width, petal_length=petal_length,
                                     petal_width=petal_width, classification=classification)

    class Meta:
        model = Flower
        fields = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'classification']
        read_only_fields = ['classification', ]
