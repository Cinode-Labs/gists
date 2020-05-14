import requests;

try:
    headers = {
        'authorization': "Bearer {{inserttokenhere}}",
        'cache-control': "no-cache",
    }
    filepath = r"{{insertpathtofilehere}}" 
    files = {'files':('{{insertfilenamehere}}',open(filepath,'rb'),'{{inesertcontettypeoffilehere}}') }

    url = "https://api.cinode.app/v0.1/companies/{{insertcompanyIdhere}}/candidates/{{insertcandidateIdhere}}/attachments"
    
    data ={'title':'{{titleoffilehere}}'}

    response = requests.post(url, data=data,files=files, headers=headers)    

    print(response.text)
    
    
except Exception as e:
    print ("Exception:", e)