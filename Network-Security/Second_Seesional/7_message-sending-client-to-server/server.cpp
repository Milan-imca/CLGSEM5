#include <iostream>
#include <cstring>
#include <sys/socket.h>
#include <netinet/in.h>
#include <unistd.h>

int main()
{
  int serverSocket = socket(AF_INET, SOCK_STREAM, 0);
  sockaddr_in serverAddress = {AF_INET, htons(8080), INADDR_ANY};
  bind(serverSocket, (struct sockaddr *)&serverAddress, sizeof(serverAddress));
  listen(serverSocket, 1);
  std::cout << "Server is running on port 8080..." << std::endl; // Indicating server is running
  int clientSocket = accept(serverSocket, nullptr, nullptr);
  char buffer[1024] = {0};
  recv(clientSocket, buffer, sizeof(buffer), 0);
  std::cout << "Message from client: " << buffer << std::endl;
  close(clientSocket);
  close(serverSocket);
  return 0;
}