#
#  Copyright (c) 2022 IBM Corp.
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#  http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#

from label_sleuth.models.core.catalog import ModelsCatalog
from label_sleuth.models.policy.static_model_policy import StaticModelPolicy


class ModelPolicies(object):
    """
    Model policies determine which type of classification model is used. Policies can be static, i.e. always return the
    same model type, or dynamic, e.g. a different model type is returned depending on the current iteration.
    """
    STATIC_SVM_ENSEMBLE = StaticModelPolicy(ModelsCatalog.SVM_ENSEMBLE)
    STATIC_SVM = StaticModelPolicy(ModelsCatalog.SVM_OVER_GLOVE)
    STATIC_HF_BERT = StaticModelPolicy(ModelsCatalog.HF_BERT)
