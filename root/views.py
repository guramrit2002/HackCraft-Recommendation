from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .serializers import HackathonRecordSerializer
from .recommendation import RecommendationSystemWrapper
# Create your views here.


@api_view(['POST'])
def hackathonpost(request):
    try:
        body = request.data
        hackathon_record_serialiser = HackathonRecordSerializer(data=body,many = False)
        if hackathon_record_serialiser.is_valid():
            new_record = hackathon_record_serialiser.save()
            return Response(
                {
                "message":"new record is created",
                "problem":new_record.problem_statement,
                "tag":new_record.tag,
                "tech":new_record.tech
                }
                ,status=status.HTTP_201_CREATED)
        else:
            print(hackathon_record_serialiser.errors)
            return Response({'errors':hackathon_record_serialiser.errors},status = status.HTTP_400_BAD_REQUEST)
        
    except Exception as e:
        return Response(str(e),status = status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET','POST'])
def hackathonget(request):
    try:
        prompt = request.data['prompt']
        result_obj = RecommendationSystemWrapper(prompt)
        result = result_obj.get_recommendations(prompt)
        response = {
            "hackathons":result
        }
        return Response(response,status=status.HTTP_200_OK)
    except Exception as e:
        print(e)
        return Response(str(e),status=status.HTTP_400_BAD_REQUEST)