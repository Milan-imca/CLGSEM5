#include <iostream>
#include <sys/epoll.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <unistd.h>
#include <fcntl.h>
#include <cstring>

#define PORT 8080
#define MAX_EVENTS 10
#define BUFFER_SIZE 1024

int make_socket_non_blocking(int sockfd)
{
  int flags = fcntl(sockfd, F_GETFL, 0);
  return (flags != -1 && fcntl(sockfd, F_SETFL, flags | O_NONBLOCK) != -1) ? 0 : -1;
}

int main()
{
  int server_fd = socket(AF_INET, SOCK_STREAM, 0);
  if (server_fd < 0)
  {
    std::cerr << "Socket creation failed" << std::endl;
    return -1;
  }

  make_socket_non_blocking(server_fd);

  sockaddr_in address = {AF_INET, htons(PORT), INADDR_ANY};
  if (bind(server_fd, (struct sockaddr *)&address, sizeof(address)) < 0)
  {
    std::cerr << "Bind failed" << std::endl;
    return -1;
  }

  if (listen(server_fd, SOMAXCONN) < 0)
  {
    std::cerr << "Listen failed" << std::endl;
    return -1;
  }

  int epoll_fd = epoll_create1(0);
  if (epoll_fd == -1)
  {
    std::cerr << "Epoll creation failed" << std::endl;
    return -1;
  }

  epoll_event event;
  event.events = EPOLLIN;
  event.data.fd = server_fd;
  epoll_ctl(epoll_fd, EPOLL_CTL_ADD, server_fd, &event);

  std::cout << "Server is running asynchronously on port " << PORT << std::endl;

  while (true)
  {
    epoll_event events[MAX_EVENTS];
    int n = epoll_wait(epoll_fd, events, MAX_EVENTS, -1);

    for (int i = 0; i < n; i++)
    {
      if (events[i].data.fd == server_fd)
      {
        int client_fd = accept(server_fd, nullptr, nullptr);
        if (client_fd >= 0)
        {
          make_socket_non_blocking(client_fd);
          epoll_event client_event;
          client_event.events = EPOLLIN;
          client_event.data.fd = client_fd;
          epoll_ctl(epoll_fd, EPOLL_CTL_ADD, client_fd, &client_event);
          std::cout << "New client connected" << std::endl;
        }
      }
      else
      {
        char buffer[BUFFER_SIZE] = {0};
        int count = read(events[i].data.fd, buffer, sizeof(buffer));
        if (count <= 0)
        {
          std::cout << "Client disconnected" << std::endl;
          close(events[i].data.fd);
        }
        else
        {
          std::cout << "Received: " << buffer << std::endl;
          send(events[i].data.fd, "Hello from async server", 24, 0);
        }
      }
    }
  }

  close(server_fd);
  return 0;
}
