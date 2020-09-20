## Django API | build from scratch

### 1. Install Docker and Docker Compose

Docker: `https://docs.docker.com/engine/install/debian/`

Docker Compose: `https://docs.docker.com/compose/install/`


### 2. Configuration

- Create `Dockerfile` and `requirements.txt`
- Create `app` directory
- Build and verify: `docker build .`

**Note:** To run `docker` commands as a non-root user, add the *user* to the
*docker* group `sudo usermod -aG docker <username>`


### 3. Configure Docker Compose

Compose file version reference: `https://docs.docker.com/compose/compose-file/`

- Create `docker-compose.yml`
- Build and verify: `docker-compose build`


### 4. Create Django Project

`docker-compose run app sh -c "django-admin.py startproject app ."`
