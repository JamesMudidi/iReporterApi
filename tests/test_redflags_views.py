import pytest
from flask import json
from app import app
CLIENT = app.test_client 

### Empty red-flags ###
def test_when_there_are_no_redflags():
    result = CLIENT().get('/api/v1/red-flags')
    assert result.status_code == 200
    json_data = json.loads(result.data)
    assert json_data['data'][0]['message'] == "No red-flags found. Please create one."


### Addng a new red-flag ###
def test_to_create_a_new_redflag():
    """
    Method for addng a new red-flag
    """
    result = CLIENT().post('/api/v1/red-flags', content_type='application/json',
                           data=json.dumps({"createdBy" : "James",
                                            "location" : [8.6784, 2.5673],
                                            "comment" : "land slide"}))
    assert result.status_code == 201

    json_data = json.loads(result.data)
    assert "data" in json_data
    assert json_data['data'][0]['id'] == 1
    assert json_data['data'][0]['message'] == "Created red-flag record"

    #make a get request to check whether the red-flag exists
    check_redflag = CLIENT().get('/api/v1/red-flags')
    assert check_redflag.status_code == 200
    json_data = json.loads(check_redflag.data)
    assert json_data['data'][0]['id'] == 1
    assert json_data['data'][0]['location'] == [8.6784, 2.5673]
    assert json_data['data'][0]['createdBy'] == "James"
    assert json_data['data'][0]['comment'] == "land slide"
    

### Getting all red-flags ###

def test_to_get_all_redflags():
    """
    Method for fetching all red-flags.
    """
    result = CLIENT().get('/api/v1/red-flags')
    assert result.status_code == 200
    json_data = json.loads(result.data)
    assert json_data['data'][0]['id'] == 1
    assert json_data['data'][0]['category'] == "red-flag"
    assert json_data['data'][0]['location'] == [8.6784, 2.5673]
    assert json_data['data'][0]['createdBy'] == "James"
    assert json_data['data'][0]['comment'] == "land slide"
    assert json_data['data'][0]['status'] == "draft"

### Getting a specific red-flag ###
def test_to_get_a_specific_redflags():
    """
    Method for fetching a specific red-flag
    """
    result = CLIENT().get('/api/v1/red-flags/1')
    assert result.status_code == 200
    json_data = json.loads(result.data)
    assert json_data['data']['id'] == 1
    assert json_data['data']['category'] == "red-flag"
    assert json_data['data']['location'] == [8.6784, 2.5673]
    assert json_data['data']['createdBy'] == "James"
    assert json_data['data']['comment'] == "landslide"
    assert json_data['data']['status'] == "draft"

### Changing geolocation ###
def test_to_change_geolocation_of_a_redflag():
    """
    Method for changing geolocation
    """
    result = CLIENT().put('/api/v1/red-flags/1', content_type='application/json',
                           data=json.dumps({"location" : [0.9090,5.9090]}))
    
    assert result.status_code == 200

    json_data = json.loads(result.data)
    assert "data" in json_data
    assert json_data['data'][0]['id'] == 1
    assert json_data['data'][0]['message'] == "Updated red-flag record’s location"

    #make a put request to check whether the red-flag has been updated
    check_redflag = CLIENT().get('/api/v1/red-flags/1')
    assert check_redflag.status_code == 200
    json_data = json.loads(check_redflag.data)
    assert json_data['data']['id'] == 1
    assert json_data['data']['location'] == [0.9090,5.9090]
    assert json_data['data']['category'] == "red-flag"
    assert json_data['data']['createdBy'] == "James"
    assert json_data['data']['comment'] == "land slide"
    assert json_data['data']['status'] == "draft"

### Deleting a red flag ###
def test_to_delete_a_redflag():
    result = CLIENT().delete('/api/v1/red-flags/1', content_type='application/json',
                           data=json.dumps({"createdBy":"James"}))
    
    assert result.status_code == 200

    json_data = json.loads(result.data)
    assert "data" in json_data
    assert json_data['data'][0]['id'] == '1'
    assert json_data['data'][0]['message'] == "red-flag record has been deleted"

    # check to verify whether the red-flag has been deleted
    result = CLIENT().get('/api/v1/red-flags/1')
    assert result.status_code == 200
    json_data = json.loads(result.data)
    assert json_data['data'][0]['error-message'] == "No red-flag found"

### Updating the status of a red-flag ###
def test_for_updating_redflag_status():
    # make sure there is a red-flag to update
    test_to_create_a_new_redflag()

    result = CLIENT().put('/api/v1/update-red-flags/1', content_type='application/json',
                           data=json.dumps({"status" : "under investigation"}))

    assert result.status_code == 200

    json_data = json.loads(result.data)
    assert "data" in json_data
    assert json_data['data'][0]['id'] == 1
    assert json_data['data'][0]['message'] == "Updated red-flag record’s location"

### Checking if user can delete a red-flag when the status is updated ####  
def test_to_delete_a_redlag_after_status_update():
    result = CLIENT().delete('/api/v1/red-flags/1', content_type='application/json',
                                        data=json.dumps({"createdBy":"James"}))
    assert result.status_code == 200
    json_data = json.loads(result.data)
    assert json_data['data'][0]['error-message'] == "You can no longer edit or delete this red-flag"

### Checking if user can change geolocation after red-flag status update ####  
def test_to_change_geolocation_after_status_update():
    result = CLIENT().put('/api/v1/red-flags/1', content_type='application/json',
                           data=json.dumps({"location" : [0.9090,5.9090]}))
    assert result.status_code == 200
    json_data = json.loads(result.data)
    assert json_data['data'][0]['error-message'] == "You can no longer edit or delete this red-flag"

### Updating the status of a red-flag ###
def test_for_updating_redflag_status_with_wrong_values():
    
    result1 = CLIENT().put('/api/v1/update-red-flags/1', content_type='application/json',
                           data=json.dumps({"status" : "new status"}))
    result2 = CLIENT().put('/api/v1/update-red-flags/1', content_type='application/json',
                           data=json.dumps({}))
    result3 = CLIENT().put('/api/v1/update-red-flags/-1', content_type='application/json',
                           data=json.dumps({}))  
    result4 = CLIENT().put('/api/v1/update-red-flags/james', content_type='application/json',
                           data=json.dumps({}))
    result5 = CLIENT().put('/api/v1/update-red-flags/1', content_type='text',
                           data=json.dumps({}))

    assert result1.status_code == 200
    assert result2.status_code == 200
    assert result3.status_code == 200
    assert result4.status_code == 200
    assert result5.status_code == 200

    json_data1 = json.loads(result1.data)
    json_data2 = json.loads(result2.data)
    json_data3 = json.loads(result3.data)
    json_data4 = json.loads(result4.data)
    json_data5 = json.loads(result5.data)

    assert "data" in json_data1
    assert "data" in json_data2
    assert "data" in json_data3
    assert "data" in json_data4
    assert "data" in json_data5
  
    assert json_data1['data'][0]['error-message'] == "The status can either be 'under investigation', 'rejected', or 'resolved'"
    assert json_data2['data'][0]['error-message'] =="wrong body format. follow this example ->> {'status':'under investigation'}"
    assert json_data3['data'][0]['error-message'] == "id cannot be a negative"
    assert json_data4['data'][0]['error-message'] == "id should be a non negative integer"
    assert json_data5['data'][0]['error-message'] == "Content-type must be json"

### Change geolocation of redflag with wrong values ###
def test_to_change_geolocation_of_a_redflag_with_wrong_values():
    """
    Method for changing geolocation
    """
    result1 = CLIENT().put('/api/v1/red-flags/1', content_type='application/json',
                           data=json.dumps({"location" : 4}))
    result2 = CLIENT().put('/api/v1/red-flags/1', content_type='application/json',
                           data=json.dumps({"location" : "fhfhf"}))
    result3 = CLIENT().put('/api/v1/red-flags/1', content_type='application/json',
                           data=json.dumps({"location" : True}))
    result4 = CLIENT().put('/api/v1/red-flags/james', content_type='application/json',
                           data=json.dumps({"location" : [2,2]}))   
    result5 = CLIENT().put('/api/v1/red-flags/1', content_type='application/json',
                           data=json.dumps({"location" : ["2","2"]}))
    result6 = CLIENT().put('/api/v1/red-flags/1', content_type='application/json',
                           data=json.dumps({"location" : [2,2,2]}))
    result7 = CLIENT().put('/api/v1/red-flags/-1', content_type='application/json',
                           data=json.dumps({"location" : [2,2]}))

    results = [result1, result2, result3]
    for result in results:
        assert result.status_code == 200

        json_data = json.loads(result.data)
        assert "data" in json_data
        assert json_data['data'][0]['error-message'] == "wrong body format. follow this example ->> {'status':'under investigation'}"
        assert json_data['status'] == 400

    json_data4 = json.loads(result4.data)
    json_data5 = json.loads(result5.data)
    json_data6 = json.loads(result6.data)
    json_data7 = json.loads(result7.data)
    
    assert json_data4['data'][0]['error-message'] == "id should be a non negative integer"
    assert json_data5['data'][0]['error-message'] == ["location should contain only integers or floats"]
    assert json_data6['data'][0]['error-message'] == ["location expects only two parameters in the list"]
    assert json_data7['data'][0]['error-message'] == "id should be a non negative integer"

### Updating a red-flag that doesn't exist ###
def test_to_update_a_redflag_which_doesnt_exist():
    result1 = CLIENT().put('/api/v1/red-flags/10000', content_type='application/json',
                                        data=json.dumps({"location" : [2,3]}))
    result2 = CLIENT().put('/api/v1/update-red-flags/100000', content_type='application/json',
                           data=json.dumps({"status" : "under investigation"}))

    results = [result1, result2]
    for result in results:
        assert result.status_code == 200
        json_data = json.loads(result.data)
        assert "data" in json_data
        assert json_data['data'][0]['error-message'] == "No red-flag found"
        assert json_data['status'] == 404

### Deleting a red-flag that doesn't exist ###
def test_to_delete_a_redflag_which_doesnt_exist():
    result = CLIENT().delete('/api/v1/red-flags/10000', content_type='application/json',
                                        data=json.dumps({"createdBy" : "James"}))

    assert result.status_code == 200
    json_data = json.loads(result.data)
    assert "data" in json_data
    assert json_data['data'][0]['error-message'] == "No red-flag found"
    assert json_data['status'] == 404

### Getting a red-flag that doesn't exist ###
def test_to_get_a_redflag_which_doesnt_exist():
    result1 = CLIENT().get('/api/v1/red-flags/10000')
    result2 = CLIENT().get('/api/v1/red-flags/-3')
    result3 = CLIENT().get('/api/v1/red-flags/james')

    assert result1.status_code == 200
    assert result2.status_code == 200
    assert result3.status_code == 200

    json_data1 = json.loads(result1.data)
    json_data2 = json.loads(result2.data)
    json_data3 = json.loads(result3.data)

    assert "data" in json_data1
    assert "data" in json_data2
    assert "data" in json_data3

    assert json_data1['data'][0]['error-message'] == "No red-flag found"
    assert json_data2['data'][0]['error-message'] == "id should be a non negative integer"
    assert json_data3['data'][0]['error-message'] == "id should be a non negative integer"

    assert json_data1['status'] == 404
    assert json_data2['status'] == 400
    assert json_data3['status'] == 400

### Making a request with data which is not in json format ###
def test_to_make_a_request_with_wrong_content_type():
    result1 = CLIENT().post('/api/v1/red-flags', content_type='text',
                           data=json.dumps({"createdBy" : "James",
                                            "location" : [8.6784, 2.5673],
                                            "comment" : "land slide"}))
    result2 = CLIENT().put('/api/v1/red-flags/1', content_type='text',
                                        data=json.dumps({"location" : [2,3]}))
    result3 = CLIENT().delete('/api/v1/red-flags/1', content_type='text',
                                        data=json.dumps({"createdBy" : "James"}))
    results = [result1, result2, result3]
    for result in results:
        assert result.status_code == 200
        json_data = json.loads(result.data)
        assert "data" in json_data
        assert json_data['data'][0]['error-message'] == "Content-type must be json"
        assert json_data['status'] == 202

### Create a red-flag with wrong data ###
def test_to_create_a_redflag_with_wrong_data():
    result1= CLIENT().post('/api/v1/red-flags', content_type='application/json',
                           data=json.dumps({}))
     
    result2 = CLIENT().post('/api/v1/red-flags', content_type='application/json',
                           data=json.dumps({"createdBy" : "",
                                            "location" : [],
                                            "comment" : ""}))
    result3 = CLIENT().post('/api/v1/red-flags', content_type='application/json',
                           data=json.dumps({"createdBy" : 3,
                                            "location" : False,
                                            "comment" : True}))

    result4 = CLIENT().post('/api/v1/red-flags', content_type='application/json',
                           data=json.dumps({"createdBy" : "James",
                                            "location" : ["12.3453", "45.2123"],
                                            "comment" : "land slide"}))
    
    assert result1.status_code == 200
    assert result2.status_code == 200
    assert result3.status_code == 200
    assert result4.status_code == 200
 
    json_data1 = json.loads(result1.data)
    json_data2 = json.loads(result2.data)
    json_data3 = json.loads(result3.data)
    json_data4 = json.loads(result4.data)

    assert "data" in json_data1
    assert "data" in json_data2
    assert "data" in json_data3
    assert "data" in json_data4

    assert json_data1['data'][0]['error-message'] == "wrong body format. follow this example ->> {'createdBy':​James​, 'location':​​[12.4567,3.6789]​, 'comment': '​land slide'"
    assert json_data2['data'][0]['error-message'] == ["createdBy, location, and comment cannot be empty.","location expects only two parameters in the list"]
    assert json_data3['data'][0]['error-message'] == [
                                                        "createdBy, location, and comment cannot be empty.",
                                                        "createdBy should be a string",
                                                        "wrong location format. follow this example ->> {'location':[12.3453,9.6589]}",
                                                        "comment should be string"
                                                    ]
    assert json_data4['data'][0]['error-message'] == ["location should contain only integers or floats"]
    
### Deleting a red-flag with wrong username ###
def test_delete_redflag_with_wrong_username():
    result1 = CLIENT().delete('/api/v1/red-flags/1', content_type='application/json',
                                        data=json.dumps({"createdBy":"dgfhdjdj"}))
    result2 = CLIENT().delete('/api/v1/red-flags/1', content_type='application/json',
                                        data=json.dumps({}))
    assert result1.status_code == 200
    assert result2.status_code == 200
    json_data1 = json.loads(result1.data)
    json_data2 = json.loads(result2.data)

    assert json_data1['data'][0]['error-message'] == "invalid username"
    assert json_data2['data'][0]['error-message'] ==  "username is missing. follow this example ->> {'createdBy':'James']}"

### Checking if a red-flag already exists ###
def test_whether_a_redflag_already_exists():
    result = CLIENT().post('/api/v1/red-flags', content_type='application/json',
                           data=json.dumps({"createdBy" : "James",
                                            "location" : [8.6784, 2.5673],
                                            "comment" : "land slide"}))
    assert result.status_code == 200

    json_data = json.loads(result.data)
    assert "data" in json_data
    assert json_data['data'][0]['error-message'] == "This red-flag already exists, please create a new one."                                     

### Deleting a red-flag using a wrong id ###
def test_to_delete_a_redflag_using_a_wrong_id():
    result1 = CLIENT().delete('/api/v1/red-flags/james', content_type='application/json',
                                        data=json.dumps({"createdBy" : "James"}))
    result2 = CLIENT().delete('/api/v1/red-flags/-1', content_type='application/json',
                                        data=json.dumps({"createdBy" : "James"}))

    assert result1.status_code == 200
    assert result2.status_code == 200
    json_data1 = json.loads(result1.data)
    json_data2 = json.loads(result2.data)
    assert "data" in json_data1
    assert "data" in json_data2

    assert json_data1['data'][0]['error-message'] == "id should be a non negative integer"
    assert json_data2['data'][0]['error-message'] == "id should be a non negative integer"
    assert json_data1['status'] == 400
    assert json_data2['status'] == 400