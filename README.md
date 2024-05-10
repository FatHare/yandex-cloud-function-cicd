### Template gitlab CI/CD for yandex cloud function.

Steps:

1. Create a Yandex function.
   
2. Add CI/CD variable SA_YC_PRIVATE_KEY, example:
   
```json
{
    "id": "****************",
    "service_account_id": "****************",
    "created_at": "2024-05-06T13:00:46.589768914Z",
    "key_algorithm": "RSA_2048",
    "public_key": "****************",
    "private_key": "********************"
}
```

3. Fill in the variables in the .gitlab-ci.yml file

4. Done.

#### Did it help? Please give it a star.
