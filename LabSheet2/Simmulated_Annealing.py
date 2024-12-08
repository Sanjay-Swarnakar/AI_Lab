import math
import random
import matplotlib.pyplot as plt

class SimulatedAnnealingDemo:
    def __init__(self, initial_temperature, cooling_rate, iterations):
        """
        :param initial_temperature: Starting temperature
        :param cooling_rate: Rate at which temperature decreases
        :param iterations: Number of iterations
        """
        self.initial_temperature = initial_temperature
        self.cooling_rate = cooling_rate
        self.iterations = iterations
        self.temperature_schedule = []
        self.probabilities = []

    def probability_of_acceptance(self, delta_e, temperature):
        """Calculate the probability of accepting an inferior node."""
        if delta_e < 0:
            return 1.0  # Always accept better solutions
        return math.exp(-delta_e / temperature)

    def simulate(self):
        """Simulate the effect of temperature on probability."""
        temperature = self.initial_temperature
        delta_e = 10  # Assume a constant cost difference for demonstration

        for step in range(self.iterations):
            probability = self.probability_of_acceptance(delta_e, temperature)
            self.temperature_schedule.append(temperature)
            self.probabilities.append(probability)

            # Cool down the temperature
            temperature *= self.cooling_rate

    def plot_results(self):
        """Plot temperature vs. probability."""
        plt.figure(figsize=(10, 5))
        plt.plot(self.temperature_schedule, self.probabilities, marker='o')
        plt.title("Effect of Temperature on Probability of Accepting Inferior Nodes")
        plt.xlabel("Temperature")
        plt.ylabel("Probability of Acceptance")
        plt.grid()
        plt.show()

# Parameters
initial_temperature = 100  # High starting temperature
cooling_rate = 0.9  # Exponential decay factor
iterations = 50  # Number of iterations

# Create and run the simulation
simulation = SimulatedAnnealingDemo(initial_temperature, cooling_rate, iterations)
simulation.simulate()
simulation.plot_results()