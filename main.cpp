#include <iostream>
#include <chrono>
#include <thread>

class Vector3 {
public:
    float x, y, z;
    Vector3(float x_, float y_, float z_) : x(x_), y(y_), z(z_) {}
    Vector3 operator*(float scalar) const {
        return Vector3(x * scalar, y * scalar, z * scalar);
    }
};

class Transform {
public:
    void Rotate(const Vector3& rotation) {
        // This is a placeholder for rotation logic.
        // In a real application, you would update the object's rotation state here.
        std::cout << "Rotating by (" << rotation.x << ", " << rotation.y << ", " << rotation.z << ") degrees\n";
    }
};

class DayNightCycle {
public:
    float rotation = 15.0f; // Rotates 15° per second (1 day = 24 seconds)
    Transform transform;

    void Start() {
        // Initialization code if needed
    }

    void Update(float deltaTime) {
        transform.Rotate(Vector3(rotation, 0, 0) * deltaTime);
    }
};

int main() {
    DayNightCycle cycle;
    cycle.Start();

    auto previous = std::chrono::steady_clock::now();

    while (true) {
        auto current = std::chrono::steady_clock::now();
        std::chrono::duration<float> elapsed = current - previous;
        previous = current;

        cycle.Update(elapsed.count());

        std::this_thread::sleep_for(std::chrono::milliseconds(16)); // Approximate 60 FPS
    }

    return 0;
}