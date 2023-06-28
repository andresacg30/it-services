# IT Services

## API Summary

| Description | Method | Endpoint
| ----------- | ----------- | ----------- |
| Get user info | `POST` | `/api/user/info` 
| Send job and process request | `POST` | `/api/process-job?jobType`


### **/api/user/info** `POST`:
> We are going to use ipinfo.io to get the user country, city, region and other information.
- **Headers**:
    - Content-Type: application/json
    - X-API-Key: (Secret)
- **Body**:
    - ip: string
- **Response**:
    - data: object
        - ip: string
        - hostname: string
        - city: string
        - region: string
        - country: string
        - loc: string
        - org: string
        - postal: string
        - timezone: string
- **Example**
  - Request `POST /api/user/info`:
  ```json
    {
        "ip": "00.00.0.0"
    }
  ```
  - Response:
  ```json
      {
          "data": {
                "ip": "00.00.0.0",
                "hostname": "c-67-191-231-203.hsd1.ga.comcast.net",
                "city": "Atlanta",
                "region": "Georgia",
                "country": "US",
                "loc": "33.7490,-84.3880",
                "org": "AS7922 Comcast Cable Communications, LLC",
                "postal": "30318",
                "timezone": "America/New_York"
            }
        }
    ```

### **/api/process-job?jobType** `POST`:
> This endpoint is going to process the job and return the result. It can have different job types which are going to be requested in the query string.

- **Headers**:
    - Content-Type: application/json
    - X-API-Key: (Secret)
- **Body**:
    - file: file
- **Response**:
    - file: file
  
- **Example**
    - Request `POST /api/process-job?jobType=pdf-to-word`:
    ```json
        {
            "file": "file.pdf"
        }
    ```
    - Response:
    ```json
        {
            "file": "file.word"
        }
    ```