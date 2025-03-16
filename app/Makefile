# Filename Makefile

RUNTIME ?= podman
NAME ?= $(shell basename $(CURDIR))
IMAGE ?= $(NAME):latest

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

.PHONY: clean
clean:
	$(RUNTIME) rm -f $(NAME)
