# 接口调用说明

> 来源：Obsidian/30-项目与实践/项目说明/图书管理系统说明/接口调用说明.md

### 1. `UserController.java`

#### 登录

- **POST /api/users/login**
  - **描述：** 验证用户身份并在成功登录后返回令牌。
  - **方法：** `POST`
  - **URL：** `/api/users/login`
  - **请求体：**

    ```JSON
    {
      "username": "your_username",
      "password": "your_password"
    }
    ```

  - **响应：**
    - **成功 (200 OK)：** `Response<Map<String, Object>>` - 包含令牌（例如JWT）的成功响应。

      ```JSON
      {
        "code": 200,
        "message": "Success",
        "data": {
          "accessToken": "...",
          "refreshToken": "..."
        }
      }
      ```

    - **错误 (例如，400 Bad Request)：** `Response<Map<String, Object>>` - 包含错误信息的错误响应。

      ```JSON
      {
        "code": 500,
        "message": "Error message from exception",
        "data": null
      }
      ```

#### 获取登录用户数据

- **GET /api/users/info**
  - **描述：** 获取当前认证用户的信息。
  - **方法：** `GET`
  - **URL：** `/api/users/info`
  - **请求头：**
    - `Authorization`: `Bearer <your_access_token>`
  - **请求体：** 无
  - **响应：**
    - **成功 (200 OK)：** `Response<UserResponseDTO>` - 包含用户详细信息的成功响应。

      ```JSON
      {
        "code": 200,
        "message": "Success",
        "data": {
          "userId": 1,
          "username": "john.doe",
          "email": "john.doe@example.com",
          "phone": "123-456-7890",
          "registrationDate": "2023-01-01T10:00:00"
        }
      }
      ```

    - **错误 (例如，401 Unauthorized, 404 Not Found)：** `Response<UserResponseDTO>` - 包含错误信息的错误响应。

      ```JSON
      {
        "code": 500,
        "message": "Error message from exception",
        "data": null
      }
      ```

#### 添加用户

- **POST /api/users**
  - **描述：** 向系统中添加一个新用户。
  - **方法：** `POST`
  - **URL：** `/api/users`
  - **请求体：**

    ```JSON
    {
      "username": "newuser",
      "password": "securepassword",
      "email": "newuser@example.com",
      "phone": "987-654-3210"
    }
    ```

  - **响应：**
    - **成功 (200 OK)：** `Response<User>` - 包含已添加用户对象的成功响应。

      ```JSON
      {
        "code": 200,
        "message": "Success",
        "data": {
          "userId": 2,
          "username": "newuser",
          "email": "newuser@example.com",
          "phone": "987-654-3210",
          "registrationDate": "2023-06-15T14:30:00"
        }
      }
      ```

    - **错误 (例如，400 Bad Request)：** `Response<User>` - 包含错误信息的错误响应。

      ```JSON
      {
        "code": 500,
        "message": "Error message from exception",
        "data": null
      }
      ```

#### 根据ID检索用户

- **GET /api/users/{id}**
  - **描述：** 根据ID检索用户。
  - **方法：** `GET`
  - **URL：** `/api/users/{id}` （将 `{id}` 替换为实际的用户ID）
  - **请求体：** 无
  - **响应：**
    - **成功 (200 OK)：** `Response<UserResponseDTO>` - 包含用户详细信息的成功响应。

      ```JSON
      {
        "code": 200,
        "message": "Success",
        "data": {
          "userId": 1,
          "username": "john.doe",
          "email": "john.doe@example.com",
          "phone": "123-456-7890",
          "registrationDate": "2023-01-01T10:00:00"
        }
      }
      ```

    - **错误 (例如，404 Not Found)：** `Response<UserResponseDTO>` - 包含错误信息的错误响应。

      ```JSON
      {
        "code": 500,
        "message": "Error message from exception",
        "data": null
      }
      ```

#### 根据ID删除用户

- **DELETE /api/users/{id}**
  - **描述：** 根据ID删除用户。
  - **方法：** `DELETE`
  - **URL：** `/api/users/{id}` （将 `{id}` 替换为实际的用户ID）
  - **请求体：** 无
  - **响应：**
    - **成功 (200 OK)：** `Response<Void>` - 不带数据的成功响应。

      ```JSON
      {
        "code": 200,
        "message": "Success",
        "data": null
      }
      ```

    - **错误 (例如，404 Not Found)：** `Response<Void>` - 包含错误信息的错误响应。

      ```JSON
      {
        "code": 500,
        "message": "Error message from exception",
        "data": null
      }
      ```

#### 更新用户信息

- **PUT /api/users/{id}**
  - **描述：** 更新现有用户的信息。
  - **方法：** `PUT`
  - **URL：** `/api/users/{id}` （将 `{id}` 替换为实际的用户ID）
  - **请求体：**

    ```JSON
    {
      "username": "updated_username",
      "email": "updated_email@example.com",
      "phone": "111-222-3333"
      // 如果要更新密码，也可以包含在内
    }
    ```

  - **响应：**
    - **成功 (200 OK)：** `Response<UserResponseDTO>` - 包含更新后用户详细信息的成功响应。

      ```JSON
      {
        "code": 200,
        "message": "Success",
        "data": {
          "userId": 1,
          "username": "updated_username",
          "email": "updated_email@example.com",
          "phone": "111-222-3333",
          "registrationDate": "2023-01-01T10:00:00"
        }
      }
      ```

    - **错误 (例如，404 Not Found, 400 Bad Request)：** `Response<UserResponseDTO>` - 包含错误信息的错误响应。

      ```JSON
      {
        "code": 500,
        "message": "Error message from exception",
        "data": null
      }
      ```

#### 获取用户列表

- **GET /api/users**
  - **描述：** 获取用户列表，可选择通过筛选条件进行过滤。
  - **方法：** `GET`
  - **URL：** `/api/users`
  - **查询参数 (可选)：**
    - `keyword`: 在用户字段（例如，用户名、电子邮件、电话）中搜索的通用关键字。
    - `phone`: 根据电话号码过滤用户。
    - `email`: 根据电子邮件地址过滤用户。
    - `date`: 根据注册日期过滤用户（精确匹配）。格式：`yyyy-MM-ddTHH:mm:ss`。
    - `startDate`: 过滤在此日期或之后注册的用户。格式：`yyyy-MM-ddTHH:mm:ss`。
    - `endDate`: 过滤在此日期或之前注册的用户。格式：`yyyy-MM-ddTHH:mm:ss`。
  - **请求体：** 无
  - **响应：**
    - **成功 (200 OK)：** `Response<List<UserResponseDTO>>` - 包含用户详细信息列表的成功响应。

      ```JSON
      {
        "code": 200,
        "message": "Success",
        "data": [
          {
            "userId": 1,
            "username": "john.doe",
            "email": "john.doe@example.com",
            "phone": "123-456-7890",
            "registrationDate": "2023-01-01T10:00:00"
          },
          {
            "userId": 3,
            "username": "jane.smith",
            "email": "jane.smith@example.com",
            "phone": "999-888-7777",
            "registrationDate": "2023-02-10T11:00:00"
          }
        ]
      }
      ```

    - **错误 (例如，日期格式无效的 400 Bad Request)：** `Response<List<UserResponseDTO>>` - 包含错误信息的错误响应。

      ```JSON
      {
        "code": 500,
        "message": "Error message from exception",
        "data": null
      }
      ```

### 2. `BookController.java`

#### 添加新书

- **POST /api/books**
  - **描述：** 向图书馆添加一本新书。
  - **方法：** `POST`
  - **URL：** `/api/books`
  - **请求体：**

    ```JSON
    {
      "title": "The Great Gatsby",
      "author": "F. Scott Fitzgerald",
      "isbn": "978-0743273565",
      "category": "Classic",
      "copiesAvailable": 5
    }
    ```

  - **响应：**
    - **成功 (200 OK)：** `Response<Book>` - 包含已添加图书对象的成功响应。

      ```JSON
      {
        "code": 200,
        "message": "Success",
        "data": {
          "bookId": 101,
          "title": "The Great Gatsby",
          "author": "F. Scott Fitzgerald",
          "isbn": "978-0743273565",
          "category": "Classic",
          "copiesAvailable": 5
        }
      }
      ```

    - **错误 (例如，400 Bad Request)：** `Response<Book>` - 包含错误信息的错误响应。

      ```JSON
      {
        "code": 500,
        "message": "Error message from exception",
        "data": null
      }
      ```

#### 根据ID删除图书

- **DELETE /api/books/{id}**
  - **描述：** 根据ID删除图书。
  - **方法：** `DELETE`
  - **URL：** `/api/books/{id}` （将 `{id}` 替换为实际的图书ID）
  - **请求体：** 无
  - **响应：**
    - **成功 (200 OK)：** `Response<Void>` - 不带数据的成功响应。

      ```JSON
      {
        "code": 200,
        "message": "Success",
        "data": null
      }
      ```

    - **错误 (例如，404 Not Found)：** `Response<Void>` - 包含错误信息的错误响应。

      ```JSON
      {
        "code": 500,
        "message": "Error message from exception",
        "data": null
      }
      ```

#### 更新图书的信息

- **PUT /api/books/{id}**
  - **描述：** 更新现有图书的信息。
  - **方法：** `PUT`
  - **URL：** `/api/books/{id}` （将 `{id}` 替换为实际的图书ID）
  - **请求体：**

    ```JSON
    {
      "title": "The Great Gatsby (Revised Edition)",
      "author": "F. Scott Fitzgerald",
      "category": "Fiction",
      "copiesAvailable": 3
    }
    ```

  - **响应：**
    - **成功 (200 OK)：** `Response<Book>` - 包含更新后图书对象的成功响应。

      ```JSON
      {
        "code": 200,
        "message": "Success",
        "data": {
          "bookId": 101,
          "title": "The Great Gatsby (Revised Edition)",
          "author": "F. Scott Fitzgerald",
          "isbn": "978-0743273565",
          "category": "Fiction",
          "copiesAvailable": 3
        }
      }
      ```

    - **错误 (例如，404 Not Found, 400 Bad Request)：** `Response<Book>` - 包含错误信息的错误响应。

      ```JSON
      {
        "code": 500,
        "message": "Error message from exception",
        "data": null
      }
      ```

#### 根据ID检索图书

- **GET /api/books/{id}**
  - **描述：** 根据ID检索图书。
  - **方法：** `GET`
  - **URL：** `/api/books/{id}` （将 `{id}` 替换为实际的图书ID）
  - **请求体：** 无
  - **响应：**
    - **成功 (200 OK)：** `Response<Book>` - 包含图书详细信息的成功响应。

      ```JSON
      {
        "code": 200,
        "message": "Success",
        "data": {
          "bookId": 101,
          "title": "The Great Gatsby",
          "author": "F. Scott Fitzgerald",
          "isbn": "978-0743273565",
          "category": "Classic",
          "copiesAvailable": 5
        }
      }
      ```

    - **错误 (例如，404 Not Found)：** `Response<Book>` - 包含错误信息的错误响应。

      ```JSON
      {
        "code": 500,
        "message": "Error message from exception",
        "data": null
      }
      ```

#### 获取图书列表

- **GET /api/books**
  - **描述：** 获取图书列表，可选择通过书名、作者或类别进行筛选。
  - **方法：** `GET`
  - **URL：** `/api/books`
  - **查询参数 (可选 - _如果提供多个过滤器，则只应用一个，根据代码中的条件顺序：书名，然后作者，然后类别_)：**
    - `title`: 根据书名过滤图书（部分匹配）。
    - `author`: 根据作者过滤图书（部分匹配）。
    - `category`: 根据类别过滤图书（精确匹配）。
  - **请求体：** 无
  - **响应：**
    - **成功 (200 OK)：** `Response<Map<String, Object>>` - 包含图书列表和总数的成功响应。

```JSON
            {
              "code": 200,
              "message": "Success",
              "data": {
                "records": [
                  {
                    "bookId": 101,
                    "title": "The Great Gatsby",
                    "author": "F. Scott Fitzgerald",
                    "isbn": "978-0743273565",
                    "category": "Classic",
                    "copiesAvailable": 5
                  },
                  {
                    "bookId": 102,
                    "title": "To Kill a Mockingbird",
                    "author": "Harper Lee",
                    "isbn": "978-0446310789",
                    "category": "Fiction",
                    "copiesAvailable": 3
                  }
                ],
                "total": 2
              }
            }
```

- **错误 (例如，500 Internal Server Error)：** `Response<Map<String, Object>>` - 包含错误信息的错误响应。

```JSON
            {
              "code": 500,
              "message": "Error message from exception",
              "data": null
            }
```

### 3. `BorrowRecordController.java`

#### 借书

- **POST /api/borrow-records**
  - **描述：** 添加一条新的借阅记录。
  - **方法：** `POST`
  - **URL：** `/api/borrow-records`
  - **请求体：**

    ```JSON
    {
      "userId": 1,
      "bookId": 101,
      "borrowDate": "2023-06-15T10:00:00"
      // returnDate 初始时可能为 null
    }
    ```

  - **响应：**
    - **成功 (200 OK)：** `Response<BorrowRecord>` - 包含已添加借阅记录的成功响应。

      ```JSON
      {
        "code": 200,
        "message": "Success",
        "data": {
          "recordId": 1,
          "userId": 1,
          "bookId": 101,
          "borrowDate": "2023-06-15T10:00:00",
          "returnDate": null
        }
      }
      ```

    - **错误 (例如，400 Bad Request，如果图书不可用)：** `Response<BorrowRecord>` - 包含错误信息的错误响应。

      ```JSON
      {
        "code": 500,
        "message": "Error message from exception",
        "data": null
      }
      ```

#### 获取所有借阅记录

- **GET /api/borrow-records**
  - **描述：** 获取所有借阅记录的列表。
  - **方法：** `GET`
  - **URL：** `/api/borrow-records`
  - **请求体：** 无
  - **响应：**
    - **成功 (200 OK)：** `Response<List<BorrowRecord>>` - 包含借阅记录列表的成功响应。

      ```JSON
      {
        "code": 200,
        "message": "Success",
        "data": [
          {
            "recordId": 1,
            "userId": 1,
            "bookId": 101,
            "borrowDate": "2023-06-15T10:00:00",
            "returnDate": null
          },
          {
            "recordId": 2,
            "userId": 2,
            "bookId": 102,
            "borrowDate": "2023-06-10T09:00:00",
            "returnDate": "2023-06-12T17:00:00"
          }
        ]
      }
      ```

    - **错误 (例如，500 Internal Server Error)：** `Response<List<BorrowRecord>>` - 包含错误信息的错误响应。

      ```JSON
      {
        "code": 500,
        "message": "Error message from exception",
        "data": null
      }
      ```

#### 根据用户ID检索借阅记录

- **GET /api/borrow-records/{id}**
  - **描述：** 根据ID检索特定的借阅记录。
  - **方法：** `GET`
  - **URL：** `/api/borrow-records/{id}` （将 `{id}` 替换为实际的借阅记录ID）
  - **请求体：** 无
  - **响应：**
    - **成功 (200 OK)：** `Response<BorrowRecord>` - 包含借阅记录详细信息的成功响应。

      ```JSON
      {
        "code": 200,
        "message": "Success",
        "data": {
          "recordId": 1,
          "userId": 1,
          "bookId": 101,
          "borrowDate": "2023-06-15T10:00:00",
          "returnDate": null
        }
      }
      ```

    - **错误 (例如，404 Not Found)：** `Response<BorrowRecord>` - 包含错误信息的错误响应。

      ```JSON
      {
        "code": 500,
        "message": "Error message from exception",
        "data": null
      }
      ```

#### 还书

- **PUT /api/borrow-records/{id}/return**
  - **描述：** 将给定借阅记录的图书标记为已归还。
  - **方法：** `PUT`
  - **URL：** `/api/borrow-records/{id}/return` （将 `{id}` 替换为实际的借阅记录ID）
  - **请求体：** 无
  - **响应：**
    - **成功 (200 OK)：** `Response<BorrowRecord>` - 包含更新后（带有 `returnDate`）借阅记录的成功响应。

      ```JSON
      {
        "code": 200,
        "message": "Success",
        "data": {
          "recordId": 1,
          "userId": 1,
          "bookId": 101,
          "borrowDate": "2023-06-15T10:00:00",
          "returnDate": "2023-06-15T18:00:00"
        }
      }
      ```

    - **错误 (例如，404 Not Found，或者图书已归还)：** `Response<BorrowRecord>` - 包含错误信息的错误响应。

      ```JSON
      {
        "code": 500,
        "message": "Error message from exception",
        "data": null
      }
      ```
