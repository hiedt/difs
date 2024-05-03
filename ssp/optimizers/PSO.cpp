#include <iostream>
#include <vector>
#include <random>
#include <algorithm>

// Define the problem to be optimized (example: Sphere function)
double sphere_function(const std::vector<double>& x) {
    double sum = 0.0;
    for (double xi : x) {
        sum += xi * xi;
    }
    return sum;
}

// Define a particle structure
struct Particle {
    std::vector<double> position;
    std::vector<double> velocity;
    double best_fitness;
    std::vector<double> best_position;
};

// Define the PSO class
class ParticleSwarmOptimizer {
private:
    int num_particles;
    int num_dimensions;
    std::vector<Particle> particles;
    std::vector<double> global_best_position;
    double global_best_fitness;

public:
    ParticleSwarmOptimizer(int num_particles, int num_dimensions) 
        : num_particles(num_particles), num_dimensions(num_dimensions) {
        particles.resize(num_particles);
        global_best_fitness = std::numeric_limits<double>::max();
    }

    void initialize_particles(double lower_bound, double upper_bound) {
        std::random_device rd;
        std::mt19937 gen(rd());
        std::uniform_real_distribution<double> dist(lower_bound, upper_bound);

        for (int i = 0; i < num_particles; ++i) {
            particles[i].position.resize(num_dimensions);
            particles[i].velocity.resize(num_dimensions);

            for (int j = 0; j < num_dimensions; ++j) {
                particles[i].position[j] = dist(gen);
                particles[i].velocity[j] = dist(gen);
            }

            particles[i].best_fitness = sphere_function(particles[i].position);
            particles[i].best_position = particles[i].position;

            if (particles[i].best_fitness < global_best_fitness) {
                global_best_fitness = particles[i].best_fitness;
                global_best_position = particles[i].best_position;
            }
        }
    }

    void update_particles(double inertia, double cognitive_weight, double social_weight) {
        std::random_device rd;
        std::mt19937 gen(rd());
        std::uniform_real_distribution<double> dist(0.0, 1.0);

        for (int i = 0; i < num_particles; ++i) {
            for (int j = 0; j < num_dimensions; ++j) {
                double r1 = dist(gen);
                double r2 = dist(gen);
                particles[i].velocity[j] = inertia * particles[i].velocity[j] +
                                            cognitive_weight * r1 * (particles[i].best_position[j] - particles[i].position[j]) +
                                            social_weight * r2 * (global_best_position[j] - particles[i].position[j]);
                particles[i].position[j] += particles[i].velocity[j];

                // Update best position
                double fitness = sphere_function(particles[i].position);
                if (fitness < particles[i].best_fitness) {
                    particles[i].best_fitness = fitness;
                    particles[i].best_position = particles[i].position;

                    if (particles[i].best_fitness < global_best_fitness) {
                        global_best_fitness = particles[i].best_fitness;
                        global_best_position = particles[i].best_position;
                    }
                }
            }
        }
    }

    std::vector<double> optimize(int max_iterations, double inertia, double cognitive_weight, double social_weight) {
        initialize_particles(-10.0, 10.0);

        for (int iter = 0; iter < max_iterations; ++iter) {
            update_particles(inertia, cognitive_weight, social_weight);
        }

        return global_best_position;
    }
};

int main() {
    int num_particles = 50;
    int num_dimensions = 10;
    int max_iterations = 100;
    double inertia = 0.5;
    double cognitive_weight = 2.0;
    double social_weight = 2.0;

    ParticleSwarmOptimizer pso(num_particles, num_dimensions);
    std::vector<double> solution = pso.optimize(max_iterations, inertia, cognitive_weight, social_weight);

    std::cout << "Optimal solution found: ";
    for (double x : solution) {
        std::cout << x << " ";
    }
    std::cout << std::endl;

    return 0;
}
