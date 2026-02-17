resource "yandex_compute_disk" "postgresql-disk" {
  count = 2
  name       = "pgdisk-${count.index + 1}"
  type       = "network-ssd"
  zone       = "ru-central1-d"
  size       = 30
}


resource "yandex_compute_instance" "bob4inski" {
  count = 2

  name = "bob4inski-${count.index + 1}"
  hostname = "bob4inski-${count.index + 1}"

  # остальное всё так же:
  boot_disk {
    initialize_params {
      name       = "disk-ubuntu-24-04-bob4inski-${count.index + 1}"
      type       = "network-ssd"
      size       = 20
      block_size = 4096
      image_id   = "fd8kiogst6b2vj84enm8"
    }
    auto_delete = true
  }
  # secondary_disk {
  #   disk_id = ""
  # }

  folder_id = "b1gdfsq84al32hk568ka"

  metadata = {
    user-data = file("${path.module}/users.yaml")
    ssh-keys  = <<-EOT
    root:ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBLdkCXZ3COswcvSrNYRndfbQykE1icJbMCMbZcad4Dty6JbILrbDtD89wkU1uGw57woQhaoF0yFX4P7wM/4vc40= # Skotty bob4inski@legacy
    EOT
  }

  network_interface {
    subnet_id = "fl88a0j1f1siuh3cdtf3"
    index     = 0
    nat       = true
  }

  platform_id = "standard-v3"
  resources {
    memory        = 2
    cores         = 2
  }
  scheduling_policy {
    preemptible = true
  }
  zone = "ru-central1-d"
}
