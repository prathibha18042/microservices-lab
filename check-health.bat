@echo off
echo ============================================
echo Microservices Health Check
echo ============================================
echo.

echo [1/5] Checking User Service...
curl -s http://localhost:8001/health
echo.
echo.

echo [2/5] Checking Product Service...
curl -s http://localhost:8002/health
echo.
echo.

echo [3/5] Checking Order Service...
curl -s http://localhost:8003/health
echo.
echo.

echo [4/5] Checking API Gateway...
curl -s http://localhost/health
echo.
echo.

echo [5/5] Docker Container Status:
echo ============================================
docker-compose ps
echo.

echo ============================================
echo Health Check Complete
echo ============================================
pause