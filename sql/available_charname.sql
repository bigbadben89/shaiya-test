USE PS_GameDefs
GO
SET QUOTED_IDENTIFIER OFF 
GO
SET ANSI_NULLS ON 
GO




create     Proc [dbo].[AvailiableCharName]
@charname varchar(20),
@Availiable int OUTPUT

AS

SET NOCOUNT ON

set @Availiable=1

if exists(select * from ps_gamedata.dbo.chars where charname=@charname)
begin
set @Availiable=0
end





return 

SET NOCOUNT OFF




GO
SET QUOTED_IDENTIFIER OFF 
GO
SET ANSI_NULLS ON 
GO

