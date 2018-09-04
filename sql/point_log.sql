USE PS_GameData
GO
SET QUOTED_IDENTIFIER ON 
GO
SET ANSI_NULLS ON 
GO

create   Proc [dbo].[usp_Save_User_BuyPointItems2]

@UserUID int,
@CharID int,
@UsePoint int,
@ProductCode varchar(20),
@UseDate datetime

AS

SET NOCOUNT ON
--SET XACT_ABORT ON

DECLARE @UseType 	int
DECLARE @Ret 		int
DECLARE @RemainPoint  	int
DECLARE @OrderNumber 	int
DECLARE @ReturnValue int

SET @Ret = 0

SET @UseType = 1 -- ??

BEGIN DISTRIBUTED TRANSACTION

/*========================================
??? ??
??? ?? ?? ?? UID ? ?? ?? UID? ??? ???? ???.
procRequestOrderProductByGame

???? UID       @buyClientUserNumber               BIGINT
???? UID       @receiveClientUserNumber           BIGINT
?????         @itemCode                          VARCHAR(50)
?? ??          @resultCode                        SMALLINT           	OUTPUT
?? ? ??       @cashBalanceAfterOrder             INT                      	OUTPUT
????	   @orderNumber			      INT			OUTPUT

resultCode
0            ??
1            ????
2            ?? ??? ???? ??
3            ?? ???? ???? ??
5            DB??
6            ????
=========================================*/
EXEC @ReturnValue = game.PS_UserData.dbo.usp_Update_UserPoint @UserUID, @UsePoint
IF ( @ReturnValue < 0 )
BEGIN
	GOTO ERROR
END

/*IF ( @Ret <> 0 )
BEGIN  
	INSERT INTO PointErrorLog( UserUID, CharID, ProductCode, Ret) 	VALUES( @UserUID, @CharID, @ProductCode, @Ret )
	GOTO ERROR
END
---------------------------------------------
*/

-- ??? ?? ??
INSERT INTO PointLog(UseType,UserUID,CharID,UsePoint,ProductCode,UseDate,RemainPoint,OrderNumber)
VALUES(@UseType,@UserUID,@CharID,@UsePoint,@ProductCode,@UseDate,@RemainPoint,@OrderNumber)
IF( @@ERROR<>0)
BEGIN
	GOTO ERROR
END

COMMIT TRAN
RETURN 1

ERROR:
ROLLBACK TRAN
RETURN -1


SET XACT_ABORT OFF
SET NOCOUNT OFF

GO
SET QUOTED_IDENTIFIER OFF 
GO
SET ANSI_NULLS ON 
GO

