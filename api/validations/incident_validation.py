from flask import jsonify

def validate_createdBy(createdBy):
    if not createdBy or not isinstance(createdBy, str) or createdBy.isspace():
        return jsonify({
            'status':400,
        	'message':'createdBy has to be filled with string characters only'
            }),400
    return True

def validate_images(images):
    if not images or len(images) == 0 or images.isspace():
        return jsonify ({
        	'status':400,
        	'message':'All incidents need to have images'
            }),400
    return True

def validate_videos(videos):
    if not videos or len(videos) == 0 or videos.isspace():
        return jsonify ({
        	'status':400,
        	'message':'All incidents need to have videos'
            }),400
    return True

def validate_comment(comment):
    if not comment or not isinstance(comment, str) or comment.isspace():
        return jsonify({
        	'status':400,
        	'message':'comment has to be filled with string characters only'
            }),400
    return True
