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
