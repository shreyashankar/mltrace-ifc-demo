from mltrace import Component

import numpy as np
import random
import string
import time

if __name__ == "__main__":
    c = Component(
        name="test-ifc-commit",
        owner="shreya",
        description="Measures commit time with varying amount of labels.",
        tags=["nyc-taxicab"],
    )

    @c.run(input_vars={"inputs": "labels"}, output_vars=["outputs"])
    def run_fake_computation_with_labels(inputs, labels):
        outputs = inputs * 2
        return outputs

    @c.run(input_vars=["inputs"], output_vars=["outputs"])
    def run_fake_computation_without_labels(inputs):
        outputs = inputs * 2
        return outputs

    def create_label(size=10, chars=string.ascii_uppercase):
        return "".join(random.choice(chars) for _ in range(size))

    ifc_results = {}
    without_ifc_results = {}
    for num_labels in range(1, 100, 10):
        inputs = np.random.rand(1000)
        labels = [create_label() for _ in range(num_labels)]

        # time the computation
        start_time = time.time()
        run_fake_computation_with_labels(inputs=inputs, labels=labels)
        end_time = time.time()

        # Log time
        ifc_results[num_labels] = end_time - start_time

        start_time = time.time()
        run_fake_computation_without_labels(inputs=inputs)
        end_time = time.time()
        without_ifc_results[num_labels] = end_time - start_time

    print(ifc_results)
    print(without_ifc_results)
