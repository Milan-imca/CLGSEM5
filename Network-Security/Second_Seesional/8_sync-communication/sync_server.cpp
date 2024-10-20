#include <iostream>
#include <sys/socket.h>
#include <netinet/in.h>
#include <unistd.h>
#include <cstring>

#define PORT 8080

int main() {
    // Create socket (IPv4, TCP)
    int server_fd = socket(AF_INET, SOCK_STREAM, 0);
    if (server_fd == 0) {
        std::cerr << "Socket creation failed" << std::endl;
        return -1;
    }

    // Server address
    struct sockaddr_in address = {};
    address.sin_family = AF_INET;
    address.sin_addr.s_addr = INADDR_ANY;
    address.sin_port = htons(PORT);

    // Bind socket
    if (bind(server_fd, (struct sockaddr *)&address, sizeof(address)) < 0) {
        std::cerr << "Bind failed" << std::endl;
        return -1;
    }

    // Listen for connections
    listen(server_fd, 3);
    std::cout << "Server is running on port " << PORT << "..." << std::endl;

    // Accept connection
    int new_socket = accept(server_fd, nullptr, nullptr);
    if (new_socket < 0) {
        std::cerr << "Connection failed" << std::endl;
        return -1;
    }

    std::cout << "Client connected" << std::endl;

    // Receive client message
    char buffer[1024] = {0};
    read(new_socket, buffer, sizeof(buffer));
    std::cout << "Client: " << buffer << std::endl;

    // Send response to client
    const char *response = "Hello from server";
    send(new_socket, response, strlen(response), 0);

    // Close sockets
    close(new_socket);
    std::cout << "Client disconnected" << std::endl;
    close(server_fd);
    return 0;
}
