import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
import numpy as np

# Create figure and styling for plotting
fig, ax = plt.subplots(1, 1, figsize=(6, 3))
ax.set(xlabel='dimensions (m)', ylabel='log(dmax/dmin)', title='dmax/dmin vs. dimensionality')
line_styles = {0: 'ro-', 1: 'b^-', 2: 'gs-', 3: 'cv-'}

# Plot dmax/dmin ratio
# TODO: fill in valid test numbers
for idx, num_samples in enumerate([100, 500, 1000, 5000]):

    # TODO: Fill in a valid feature range
    feature_range = range(1, 101)
    ratios = []
    for num_features in feature_range:
        # TODO: Generate synthetic data using make_classification
        X = np.random.randn(num_samples, num_features)

        
        # TODO: Choose random query point from X
        rand_point = np.random.randint(0, X.shape[0])
        query_point = X[rand_point]
        
        # TODO: remove query pt from X so it isn't used in distance calculations
        X_remaining = np.delete(X, rand_point, axis=0)

        # TODO: Calculate distances
        distances = np.linalg.norm(X_remaining - query_point, axis=1)
        ratio = np.max(distances) / np.min(distances)
        ratios.append(ratio)

        print(f"N={num_samples}, m={num_features}, ratio={ratio}")

    ax.plot(feature_range, np.log(ratios), line_styles[idx], label=f'N={num_samples:,}')

plt.legend()
plt.tight_layout()
plt.grid(True)
plt.show()