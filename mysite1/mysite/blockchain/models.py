from django.db import models

# Create your models here.
    
# This class represents a public chain block 
    

class SideChain(models.Model):
    # skipping block_id, it gets automatically generated and is auto-incrementing
    project_id=models.IntegerField()
    # block=models.ForeignKey(SideChainBlock,on_delete=models.CASCADE)

class SideChainBlock(models.Model):
    # skipping block_id, it gets automatically generated and is auto-incrementing
    block_size=models.IntegerField()
    block_version = models.CharField(max_length=20)
    project_id=models.IntegerField()
    contributor_id=models.IntegerField()
    previous_block=models.ForeignKey('self',on_delete=models.CASCADE,blank=True,null=True)#TODO
    side_chain=models.ForeignKey(SideChain,on_delete=models.CASCADE)
    timestamp=models.DateTimeField(auto_now_add=True)
    log_file=models.CharField(max_length=200)

class PublicChainBlock(models.Model):
    # skipping block_id, it gets automatically generated and is auto-incrementing
    hash = models.CharField(max_length=100) # the blocks own hash
    previous_block = models.ForeignKey('self',on_delete=models.CASCADE,blank=True,null=True) # A reference to the previous block, it will use the id instead of the hash, but that's ok.
    side_block = models.ForeignKey(SideChainBlock,on_delete=models.CASCADE)
    block_version = models.CharField(max_length=20)
    timestamp=models.DateTimeField(auto_now_add=True)
    