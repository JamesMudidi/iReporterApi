/**
 * iRepoter
 * iReporter enables any/every citizen to bring any form of corruption to the notice of appropriate authorities and the general public. Users can also report on things that need government intervention around the community  Checkout the API on [Github](https://github.com/JamesMudidi/iReporterApi/tree/develop-v2) 
 *
 * OpenAPI spec version: 2.0
 * Contact: mudidi.jimmy@gmail.com
 *
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen.git
 * Do not edit the class manually.
 */
package io.swagger.client.api

import io.swagger.client.model.Redflag
import io.swagger.client.core._
import io.swagger.client.core.CollectionFormats._
import io.swagger.client.core.ApiKeyLocations._

object RedflagApi {

  /**
   * 
   * 
   * Expected answers:
   *   code 400 :  (Invalid ID supplied)
   *   code 404 :  (Redflag not found)
   *   code 405 :  (Validation exception)
   * 
   * @param body create a redflag
   */
  def createRedflag(body: Redflag): ApiRequest[Unit] =
    ApiRequest[Unit](ApiMethods.POST, "https://virtserver.swaggerhub.com/JamesMudidi/iRepoter/1.0.0", "/redflag", "application/json")
      .withBody(body)
      .withErrorResponse[Unit](400)
      .withErrorResponse[Unit](404)
      .withErrorResponse[Unit](405)
        /**
   * 
   * 
   * Expected answers:
   *   code 400 :  (Invalid ID supplied)
   *   code 404 :  (Redflag not found)
   * 
   * @param redflagId Redflag id to delete
   * @param apiKey 
   */
  def deleteRedflag(redflagId: Long, apiKey: Option[String] = None): ApiRequest[Unit] =
    ApiRequest[Unit](ApiMethods.DELETE, "https://virtserver.swaggerhub.com/JamesMudidi/iRepoter/1.0.0", "/redflag/{redflag_id}/", "application/json")
      .withPathParam("RedflagId", redflagId)
      .withHeaderParam("api_key", apiKey)
      .withErrorResponse[Unit](400)
      .withErrorResponse[Unit](404)
        /**
   * Get all the redflags
   * 
   * Expected answers:
   *   code 200 : Seq[Redflag] (successful operation)
   *   code 400 :  (Invalid status value)
   * 
   * @param status Status values that need to be considered for filter
   */
  def findRedflagByStatus(status: Seq[String]): ApiRequest[Seq[Redflag]] =
    ApiRequest[Seq[Redflag]](ApiMethods.GET, "https://virtserver.swaggerhub.com/JamesMudidi/iRepoter/1.0.0", "/redflag/", "application/json")
      .withQueryParam("status", ArrayValues(status, MULTI))
      .withSuccessResponse[Seq[Redflag]](200)
      .withErrorResponse[Unit](400)
        /**
   * Returns a single Redflag
   * 
   * Expected answers:
   *   code 200 : Redflag (successful operation)
   *   code 400 :  (Invalid ID supplied)
   *   code 404 :  (Redflag not found)
   * 
   * Available security schemes:
   *   api_key (apiKey)
   * 
   * @param redflagId ID of Redflag to return
   */
  def getRedflagById(redflagId: Long)(implicit apiKey: ApiKeyValue): ApiRequest[Redflag] =
    ApiRequest[Redflag](ApiMethods.GET, "https://virtserver.swaggerhub.com/JamesMudidi/iRepoter/1.0.0", "/redflag/{redflag_id}", "application/json")
      .withApiKey(apiKey, "api_key", HEADER)
      .withPathParam("RedflagId", redflagId)
      .withSuccessResponse[Redflag](200)
      .withErrorResponse[Unit](400)
      .withErrorResponse[Unit](404)
        /**
   * 
   * 
   * Expected answers:
   *   code 405 :  (Invalid input)
   * 
   * @param redflagId ID of Redflag that needs to be updated
   * @param name Updated name of the Redflag
   * @param status Updated status of the Redflag
   */
  def updateRedflagWithForm(redflagId: Long, name: Option[String] = None, status: Option[String] = None): ApiRequest[Unit] =
    ApiRequest[Unit](ApiMethods.PATCH, "https://virtserver.swaggerhub.com/JamesMudidi/iRepoter/1.0.0", "/redflag/{redflag_id}/location", "application/x-www-form-urlencoded")
      .withFormParam("name", name)
      .withFormParam("status", status)
      .withPathParam("RedflagId", redflagId)
      .withErrorResponse[Unit](405)
        /**
   * 
   * 
   * Expected answers:
   *   code 405 :  (Invalid input)
   * 
   * @param redflagId ID of Redflag that needs to be updated
   * @param name Updated name of the Redflag
   * @param status Updated status of the Redflag
   */
  def updateRedflagWithForm_0(redflagId: Long, name: Option[String] = None, status: Option[String] = None): ApiRequest[Unit] =
    ApiRequest[Unit](ApiMethods.PATCH, "https://virtserver.swaggerhub.com/JamesMudidi/iRepoter/1.0.0", "/redflag/{redflag_id}/comment", "application/x-www-form-urlencoded")
      .withFormParam("name", name)
      .withFormParam("status", status)
      .withPathParam("RedflagId", redflagId)
      .withErrorResponse[Unit](405)
        /**
   * 
   * 
   * Expected answers:
   *   code 405 :  (Invalid input)
   * 
   * @param redflagId ID of Redflag that needs to be updated
   * @param name Updated name of the Redflag
   * @param status Updated status of the Redflag
   */
  def updateRedflagWithForm_1(redflagId: Long, name: Option[String] = None, status: Option[String] = None): ApiRequest[Unit] =
    ApiRequest[Unit](ApiMethods.PATCH, "https://virtserver.swaggerhub.com/JamesMudidi/iRepoter/1.0.0", "/redflag/{redflag_id}/status", "application/x-www-form-urlencoded")
      .withFormParam("name", name)
      .withFormParam("status", status)
      .withPathParam("RedflagId", redflagId)
      .withErrorResponse[Unit](405)
      

}

