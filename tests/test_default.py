def test_docker_is_installed(host):
    docker = host.package("docker")
    assert docker.is_installed

def test_docker_running_and_enabled(host):
    docker = host.service("docker")
    assert docker.is_running
    assert docker.is_enabled

def test_kubelet_is_installed(host):
    kubelet = host.package("kubelet")
    assert kubelet.is_installed

def test_kubelet_running_and_enabled(host):
    kubelet = host.service("kubelet")
    assert kubelet.is_running
    assert kubelet.is_enabled

def test_port_80_is_listening(host):
    socket = host.socket("tcp://80")
    assert(socket.is_listening)