### Как инициализировать какой-то профиль
```bash
# интерактивно создать себе профиль
yc init

export YC_TOKEN=$(yc iam create-token)
export YC_CLOUD_ID=$(yc config get cloud-id)
export YC_FOLDER_ID=$(yc config get folder-id)

yc iam service-account create --name server-manager
# get account id
yc iam service-account list

# Для доступа в S3
yc iam access-key create --service-account-name server-manager

access_key:
  id: ajedfce7iuvjv9nrhk7e
  service_account_id: aje31tvom3q9aekenifa
  created_at: "2026-02-14T07:29:37.433640238Z"
## Нам нужен key_id
  key_id: {}
secret: {}
```

1. Инициализируем бакет в s3
```bash
yc storage bucket create private-terraform

export ACCESS_KEY="<key_ID>"
export SECRET_KEY="<secret_key>"

```

### Куда смотреть за мануалами
- https://yandex.cloud/ru/docs/terraform/tutorials/terraform-modules#configure-terraform
- https://yandex.cloud/ru/docs/tutorials/infrastructure-management/terraform-quickstart#install-terraform
