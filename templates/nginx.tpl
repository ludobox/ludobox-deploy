server {
        listen          80;
        server_name     {{ domain }};
        root            {{ root }};

        access_log      {{ log }}/access.log;
        error_log       {{ log }}/error.log;

        proxy_connect_timeout 75s;
        proxy_read_timeout 300s;

        location / {
            include proxy_params;
            proxy_pass http://127.0.0.1:{{port}};
        }

        location /socket.io {
          include proxy_params;
          proxy_pass http://127.0.0.1:{{port}}/socket.io;

          proxy_set_header Host $host;
          proxy_buffering off;

          # Websockets support
          proxy_http_version 1.1;
          proxy_set_header Upgrade $http_upgrade;
          proxy_set_header Connection "upgrade";
      }

}
