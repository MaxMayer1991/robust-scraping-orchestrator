# Robust Scraping Orchestrator

A high-performance web scraping solution built with Scrapy and Selenium, containerized with Docker for easy deployment and scaling.

## 🚀 Features

- **Web Scraping**: Extracts car listings from AutoRIA with detailed information
- **Headless Chrome**: Uses Selenium with headless Chrome for JavaScript rendering
- **Asynchronous Processing**: Implements a pool of Chrome drivers for concurrent requests
- **PostgreSQL Storage**: Stores scraped data with proper schema and indexing
- **Dockerized**: Easy deployment with Docker and Docker Compose
- **Scheduled Scraping**: Built-in scheduler for periodic data collection
- **Proxy Support**: Configurable proxy settings for reliable scraping
- **User-Agent Rotation**: Prevents blocking with rotating user agents

## 🛠️ Prerequisites

- Docker 20.10+
- Docker Compose 2.0+
- Python 3.8+ (for local development)

## 🚀 Quick Start

1. **Clone the repository**
   ```bash
   git clone [https://github.com/yourusername/robust-scraping-orchestrator.git](https://github.com/yourusername/robust-scraping-orchestrator.git)
   cd robust-scraping-orchestrator
2. **Set up environment variables**
   ```bash
    cp .env.example .env
    # Edit .env with your configuration
   ```
3. **Build and start the containers**
   ```bash
    docker-compose up --build
   ```
4. **Access the services**
   - Scraper logs: docker logs -f scrapy_selenium
   - Database: postgresql://user:password@localhost:5432/dbname
   - pgAdmin: http://localhost:8080 (if enabled)
   
### 🏗️ Project Structure
   

     ├── carscraper/               # Scrapy project
     │   ├── items.py             # Data models
     │   ├── loaders.py           # Data processing
     │   ├── middlewares.py       # Custom middlewares
     │   ├── pipelines.py         # Data storage
     │   ├── settings.py          # Scrapy settings
     │   └── spiders/             # Spider implementations
     │       └── carspider.py     # Main spider
     ├── docker/                  # Docker configuration
     ├── logs/                    # Log files
     ├── .env.example             # Example environment variables
     ├── docker-compose.yml       # Docker Compose configuration
     ├── Dockerfile               # Docker build configuration
     ├── requirements.txt         # Python dependencies
     └── scheduler.py            # Scraping scheduler

### ⚙️ Configuration
Configure the application using environment variables in .env:
    
   ```ini
    # Database
    POSTGRES_DB=scrapy
    POSTGRES_USER=user
    POSTGRES_PASSWORD=password
    
    # Scraping
    SCRAPEOPS_API_KEY=your_api_key
    PROXY_URL=http://your-proxy:port
    
    # Scheduler
    SPIDER_TIME=*/30 * * * *  # Run every 30 minutes
    DUMP_TIME=0 0 * * *       # Daily dumps at midnight
   ```
### 🛠️ Development
1. **Set up virtual environment**
   ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    pip install -r requirements.txt
   ```
2. **Run the spider locally**
   ```bash
    scrapy crawl carspider
   ```
3. **Run tests**
   ```bash
    python -m pytest
   ```
### 📦 Deployment
   ```bash
   docker-compose --build up -d
   ```
Monitoring
- Logs: docker-compose logs -f
- Database: Use pgAdmin at http://localhost:8080
- Health checks: docker ps to check container status

### 🤝 Contributing
1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

### 📄 License
This project is licensed under the MIT License - see the LICENSE file for details.
### 📧 Contact
For support or questions, please contact **Maksym Plakushko** at mplakushko@gmail.com