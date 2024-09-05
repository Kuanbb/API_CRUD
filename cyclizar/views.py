from django.shortcuts import render
from django.urls import path, include
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Usuario
from .serializers import UsuaSerializer
from .forms import cadastro
import json

def form_show(request):
    form = cadastro()
    return render(request, 'form.html', {'form':form})

def tabela_show(request):
    dele = cadastro()
    return render(request, 'tabela.html', {'tabela':dele})

@api_view(['GET'])
def get_usuario(request):
    if request.method == 'GET':
        user = Usuario.objects.all()
        serializer = UsuaSerializer(user, many=True)
        return Response(serializer.data)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_by_nome(request, nick):
    try:
        user = Usuario.objects.get(pk=nick)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = UsuaSerializer(user)
        return Response(serializer.data)
    

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def controla_usuario(request):
    #ACESSAR
    if request.method == 'GET':
        try:
            if request.GET['user']:
                user_nick = request.GET['user']
                try:
                    user = Usuario.objects.get(pk=user_nick)
                except:
                    return Response(status=status.HTTP_404_NOT_FOUND)
                serializer = UsuaSerializer(user)
                return Response(serializer.data)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    #CRIAÇÃO DE DADOS
    if request.method == 'POST':
        nv_usuario = request.data
        serializer = UsuaSerializer(data=nv_usuario)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    #EDITANDO DADOS
    if request.method == 'PUT':
        nome = request.data['apelido_usuario']
        try:
            updated_user = Usuario.objects.get(pk=nome)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = UsuaSerializer(updated_user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    #DELETANDO DADOS
    if request.method == 'DELETE':
        try:
            deleta_usua = Usuario.objects.get(pk=request.data['apelido_usuario'])
            deleta_usua.delete()
            return Response(status=status.HTTP_202_ACCEPTED)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)