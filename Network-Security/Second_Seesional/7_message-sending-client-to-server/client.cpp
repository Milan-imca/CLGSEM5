#include <iostream>
#include <cstring>
#include <sys/socket.h>
#include <netinet/in.h>
#include <unistd.h>

int main() {

    int clientSocket = socket(AF_INET, SOCK_STREAM, 0);
    sockaddr_in serverAddress = {AF_INET, htons(8080), INADDR_ANY};
    connect(clientSocket, (struct sockaddr*)&serverAddress, sizeof(serverAddress));
    send(clientSocket, "Hello, server!", 15, 0);
    std::cout << "Message sent to server." << std::endl; // Indicating message is sent
    close(clientSocket);
    return 0;

}