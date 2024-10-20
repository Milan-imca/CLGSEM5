#include <iostream>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <unistd.h>
#include <cstring>

#define PORT 8080

int main() {
    // Create socket (IPv4, TCP)
    int sock = socket(AF_INET, SOCK_STREAM, 0);
    if (sock < 0) {
        std::cerr << "Socket creation failed" << std::endl;
        return -1;
    }

    // Server address
    struct sockaddr_in serv_addr = {};
    serv_addr.sin_family = AF_INET;
    serv_addr.sin_port = htons(PORT);
    inet_pton(AF_INET, "127.0.0.1", &serv_addr.sin_addr);

    // Connect to the server
    if (connect(sock, (struct sockaddr *)&serv_addr, sizeof(serv_addr)) < 0) {
        std::cerr << "Connection failed" << std::endl;
        return -1;
    }

    // Send message to server
    const char *message = "Hello from client";
    send(sock, message, strlen(message), 0);

    // Receive server response
    char buffer[1024] = {0};
    read(sock, buffer, sizeof(buffer));
    std::cout << "Server: " << buffer << std::endl;

    // Close socket
    close(sock);
    return 0;
}
