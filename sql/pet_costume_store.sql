USE PS_GameDefs
GO
SET QUOTED_IDENTIFIER OFF 
GO
SET ANSI_NULLS ON 
GO








create         Proc [dbo].[GetPetAndCostumeId]
@charname varchar(20),
@PetType     int OUTPUT,
@PetId       int OUTPUT,
@CostumeType int OUTPUT,
@CostumeId   int OUTPUT

AS

SET NOCOUNT ON

set @PetType=0
set @PetId=0
set @CostumeType=0
set @CostumeId=0

--get charid
declare @charid int
set @charid=0
select @charid=charid from ps_gamedata.dbo.chars where charname=@charname




--get all id
select @PetType=type    ,@PetId=typeid     from ps_gamedata.dbo.charitems where charid=@charid and bag=0 and slot=14

select @CostumeType=type,@CostumeId=typeid from ps_gamedata.dbo.charitems where charid=@charid and bag=0 and slot=15




return 


SET NOCOUNT OFF







GO
SET QUOTED_IDENTIFIER OFF 
GO
SET ANSI_NULLS ON 
GO

