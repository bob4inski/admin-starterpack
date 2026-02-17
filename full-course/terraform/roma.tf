resource "yandex_compute_instance" "qfunk" {
  count = 2

  name = "qfunk-${count.index + 1}"
  hostname = "qfunk-${count.index + 1}"

  # остальное всё так же:
  boot_disk {
    initialize_params {
      name       = "disk-ubuntu-24-04-qfunk-${count.index + 1}"
      type       = "network-ssd"
      size       = 20
      block_size = 4096
      image_id   = "fd8kiogst6b2vj84enm8"
    }
    auto_delete = true
  }

  folder_id = "b1gdfsq84al32hk568ka"

  metadata = {
    user-data = "#cloud-config\ndatasource:\n Ec2:\n  strict_id: false\nssh_pwauth: no\nusers:\n- name: qfunk\n  sudo: ALL=(ALL) NOPASSWD:ALL\n  shell: /bin/bash\n  ssh_authorized_keys:\n  - ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIN2DedEVBodfbLGFibZz2j/cUQ9GFDgkEQVCjfWr1CUt "
    ssh-keys  = "qfunk:ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIN2DedEVBodfbLGFibZz2j/cUQ9GFDgkEQVCjfWr1CUt "
  }

  network_interface {
    subnet_id = "fl88a0j1f1siuh3cdtf3"
    index     = 0
    nat       = true
  }
  platform_id = "standard-v3"
  resources {
    memory        = 1
    cores         = 2
    core_fraction = 20
  }
  scheduling_policy {
    preemptible = true
  }
  zone = "ru-central1-d"
}
