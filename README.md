# mltrace-ifc-demo

Description: this demo is for CS294 (Privacy-Preserving Systems).

This tutorial builds a training and testing pipeline for a toy ML prediction problem: to predict whether a passenger in a NYC taxicab ride will give the driver a nontrivial tip. This is a **binary classification task.** A nontrivial tip is arbitrarily defined as greater than 10% of the total fare (before tip). To evaluate the model or measure the efficacy of the model, we measure the [**F1 score**](https://en.wikipedia.org/wiki/F-score). This task is modeled after the task described in [toy-ml-pipeline](https://github.com/shreyashankar/toy-ml-pipeline).

The purpose of this demo is to demonstrate how we have incorporated information flow control techniques to help developers retract data from customers who request data deletion. In this demo, we:

1. Run training pipeline on Jan 2020 data
2. Run inference “weekly” from Feb 1, 2020 to May 31, 2020
3. Delete user_109 label (not used in training)
  * “Weekly” inference will still run successfully
4. Delete user_139 label (used in training)
  * Use 30-second threshold (default is 30 days)
  * “Weekly” inference will throw errors 
