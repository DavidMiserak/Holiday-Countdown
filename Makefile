# Filename Makefile

RUNTIME ?= podman
NAME ?= holiday-countdown
IMAGE ?= $(NAME):latest

.PHONY: pre-commit-setup
pre-commit-setup:
	pre-commit install
	pre-commit install --install-hooks
	pre-commit run --all-files

.PHONY: image-build
image-build: Dockerfile
	$(RUNTIME) build -t $(IMAGE) .

.PHONY: image-run
image-run: image-build
	@echo "Open http://localhost:5000"
	$(RUNTIME) run --rm -it \
	--network host \
	-p 5000:5000 \
	--name $(NAME) \
	$(IMAGE)

.PHONY: test-bdd
test-bdd:
	behave tests/features

.PHONY: clean
clean:
	$(RUNTIME) rm -f $(NAME)
